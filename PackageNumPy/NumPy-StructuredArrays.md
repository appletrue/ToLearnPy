# 结构化数组StructuredArrays

### 定义结构化数组

结构化的数据类型可以被认为是一定长度的字节序列（结构的itemsize），它被解释为一个字段集合。每个字段在结构中都有一个名称，一个数据类型和一个字节偏移量。字段的数据类型可以是任何numpy数据类型，包括其他结构化数据类型，也可以是一个子数组，其行为类似于指定形状的ndarray。字段的偏移是任意的，字段甚至可以重叠。这些偏移通常由numpy自动确定，但也可以指定。

通过dtype对象定义一个结构化数组。有几种替代方法来定义记录的字段。这些变体中的一些提供与Numeric，numarray或另一个模块的向后兼容性，并且除了这些目的之外不应该使用。这些将被如此注意。

## 结构化数据类型创建

结构化数据类型可以使用函数numpy.dtype来创建。使用参数（如提供给dtype函数关键字或dtype对象构造函数本身）通过四种可选方法之一指定记录结构。

此参数必须是以下之一：1）string，2）tuple，3）list，或4）dictionary。以下简要描述这些。

### 字符串参数

在这种简写符号中，构造函数需要一个逗号分隔的类型说明符列表，可选地包含额外的形状信息。字段的项目大小和字节偏移量是自动确定的，字段被赋予默认名称'f0'，'f1'，'f2'等。类型说明符可以采用4种不同的形式：

-1. 

```
`b1, i1, i2, i4, i8, u1, u2, u4, u8, f2, f4, f8, c8, c16, a`
(representing bytes, ints, unsigned ints, floats, complex and fixed length strings of specified byte lengths)
```

-2. 

int8,...,uint8,...,float16, float32, float64, complex64, complex128
   (this time with bit sizes)
-3. 

older Numeric/numarray type specifications (e.g. Float32).
   Don't use these in new code!
-4. 

Single character type specifiers (e.g H for unsigned short ints).
   Avoid using these unless you must. Details can be found in the   Numpy book

这些不同的样式可以混合在同一个字符串（但为什么你会想这样做？）。此外，每个类型说明符可以以重复数或形状为前缀。在这些情况下，将创建一个数组元素，即记录中的数组。该数组仍称为单个字段。一个例子：

```python
import numpy as np

x = np.zeros(3, dtype='3int8, float32, (2,3)float64')

print(x)
print(x.dtype)
#输出结果如下:
[([0, 0, 0],  0., [[ 0.,  0.,  0.], [ 0.,  0.,  0.]])
 ([0, 0, 0],  0., [[ 0.,  0.,  0.], [ 0.,  0.,  0.]])
 ([0, 0, 0],  0., [[ 0.,  0.,  0.], [ 0.,  0.,  0.]])]
[('f0', 'i1', (3,)), ('f1', '<f4'), ('f2', '<f8', (2, 3))] 

```

通过使用字符串来定义记录结构，它排除了能够在原始定义中命名字段。但是，名称可以更改，如后所示。

### 元组参数：

每个元组都有形式（fieldname，datatype，shape），其形状是可选的。fieldname是一个字符串（或元组，如果使用标题，请参阅下面的字段标题），数据类型可以是任何可转换为数据类型的对象，shape是指定子阵列形状的整数的元组。

```python
import numpy as np

a = np.dtype([('x', 'f4'), ('y', np.float32), ('z', 'f4', (2,2))])
print(np.dtype(a))
#输出结果:
[('x', '<f4'), ('y', '<f4'), ('z', '<f4', (2, 2))]
```

如果fieldname是空字符串“'，那么该字段将被赋予一个默认的f＃形式的名称，其中＃是该字段的整数索引，从左边的0开始计数；结构内字段的字节偏移和总体结构项目大小是自动确定的。

```python
import numpy as np

b = np.dtype([('x', 'f4'),('', 'i4'),('z', 'i8')])
print(np.dtype(b))
#输出结果:
[('x', '<f4'), ('f1', '<i4'), ('z', '<i8')]
```

适用于记录结构的唯一相关元组是当结构映射到现有数据类型时。这是通过在元组中配对现有数据类型与匹配的dtype定义（使用此处描述的任何变体）来完成的。

```python
import numpy as np

x = np.zeros(3, dtype=('i4',[('r','u1'), ('g','u1'), ('b','u1'), ('a','u1')]))
print(x['r'])
print(x.dtype)
#输出结果如下:
[0 0 0]
[('r', 'u1'), ('g', 'u1'), ('b', 'u1'), ('a', 'u1')]
```

在这种情况下，产生一个数组，其外观和行为就像一个简单的int32数组，但也有只使用int32的一个字节（有点像Fortran等效）的字段的定义。

### 列表参数：

在这种情况下，记录结构用元组列表定义。每个元组具有2或3个元素，指定：1）字段的名称（允许使用''），2）字段的类型，以及3）形状（可选）。例如：

```
import numpy as np

x = np.zeros(3, dtype=[('x','f4'),('y',np.float32),('value','f4',(2,2))])
# print(x['r'])
print(x.dtype)
print(x)
#输出结果如下:
[('x', '<f4'), ('y', '<f4'), ('value', '<f4', (2, 2))]
[( 0.,  0., [[ 0.,  0.], [ 0.,  0.]]) ( 0.,  0., [[ 0.,  0.], [ 0.,  0.]])
 ( 0.,  0., [[ 0.,  0.], [ 0.,  0.]])]
```

### 字典参数：

允许两种不同的形式。第一个包含一个具有两个必需键（'names'和'formats'）的字典，每个键都有一个相等大小的值列表。格式列表包含在其他上下文中允许的任何类型/形状说明符。名称必须是字符串。有两个可选键：“offsets”和“titles”。每个都必须是相应匹配的列表，其中偏移量包含每个字段的整数偏移量，标题是包含每个字段的元数据的对象（这些对象不必是字符串），其中允许值为None。举个例子：

```
import numpy as np

x = np.zeros(3, dtype={'names':['col1', 'col2'], 'formats':['i4','f4']})
print(x.dtype)
print(x)
#输出结果如下:
[('col1', '<i4'), ('col2', '<f4')]
[(0,  0.) (0,  0.) (0,  0.)]
```

允许的其他字典形式是具有指定类型，偏移和可选标题的元组值的名称键的字典。

```
import numpy as np

x = np.zeros(3, dtype={'col1':('i1',0,'title 1'), 'col2':('f4',1,'title 2')})
y = np.dtype({'names': ['col1', 'col2'],
          'formats': ['i4','f4'],
          'offsets': [0, 4],
          'itemsize': 12})
print(x.dtype)
print(x)
#输出结果如下:
[(('title 1', 'col1'), 'i1'), (('title 2', 'col2'), '<f4')]
[(0,  0.) (0,  0.) (0,  0.)]
[('col1', '<i4'), ('col2', '<f4')]
{'names':['col1','col2'], 'formats':['<i4','<f4'], 'offsets':[0,4], 'itemsize':12}
```

## 操作和现实结构化数组类型

### 访问和修改字段名称

字段名称是定义结构的dtype对象的属性。对于最后一个例子：

> > > x.dtype.names
> > > ('col1', 'col2')
> > > x.dtype.names = ('x', 'y')
> > > x
> > > array([(0, 0.0), (0, 0.0), (0, 0.0)],

```
import numpy as np

x = np.zeros(3, dtype=[('x','f4'),('y',np.float32),('value','f4',(2,2))])
print(x.dtype.names)

dtype=[(('title 1', 'x'), '|i1'), (('title 2', 'y'), '>f4')])
```

> > > x.dtype.names = ('x', 'y', 'z') # wrong number of names
> > > <type 'exceptions.ValueError'>: must replace all names at once with a sequence of length 2



### 访问字段标题

字段标题提供了一个标准位置来放置字段的关联信息。他们不必是字符串。

> > > x.dtype.fields['x'][2]
> > > 'title 1'



- 一次访问多个字段

您可以使用字段名称列表一次访问多个字段：

> > > x = np.array([(1.5,2.5,(1.0,2.0)),(3.,4.,(4.,5.)),(1.,3.,(2.,6.))],

```
    dtype=[('x','f4'),('y',np.float32),('value','f4',(2,2))])
```

请注意，x是使用元组列表创建的。

> > > x[['x','y']]
> > > array([(1.5, 2.5), (3.0, 4.0), (1.0, 3.0)],

```
 dtype=[('x', '<f4'), ('y', '<f4')])
```

> > > x[['x','value']]
> > > array([(1.5, [[1.0, 2.0], [1.0, 2.0]]), (3.0, [[4.0, 5.0], [4.0, 5.0]]),

```
  (1.0, [[2.0, 6.0], [2.0, 6.0]])],
 dtype=[('x', '<f4'), ('value', '<f4', (2, 2))])
```

字段按请求的顺序返回。：

> > > x[['y','x']]
> > > array([(2.5, 1.5), (4.0, 3.0), (3.0, 1.0)],

```
 dtype=[('y', '<f4'), ('x', '<f4')])
```



### 填充结构化数组

结构化数组可以按字段或逐行填充。

> > > arr = np.zeros((5,), dtype=[('var1','f8'),('var2','f8')])
> > > arr['var1'] = np.arange(5)

如果你逐行填充它，它需要一个元组（但不是一个列表或数组！）：

> > > arr[0] = (10,20)
> > > arr
> > > array([(10.0, 20.0), (1.0, 0.0), (2.0, 0.0), (3.0, 0.0), (4.0, 0.0)],

```
 dtype=[('var1', '<f8'), ('var2', '<f8')])
```



### 记录数组

为了方便起见，numpy提供了“记录数组”，允许通过属性而不是索引来访问结构化数组的字段。记录数组是使用ndarray，numpy.recarray的子类包装的结构化数组，它允许通过数组对象上的属性访问字段，记录数组也使用特殊的数据类型numpy.record

创建记录数组的最简单的方法是使用numpy.rec.array：

> > > recordarr = np.rec.array([(1,2.,'Hello'),(2,3.,"World")], 
> > > ...                    dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')])
> > > recordarr.bar
> > > array([ 2.,  3.], dtype=float32)
> > > recordarr[1:2]
> > > rec.array([(2, 3.0, 'World')], 

```
  dtype=[('foo', '<i4'), ('bar', '<f4'), ('baz', 'S10')])
```

> > > recordarr[1:2].foo
> > > array([2], dtype=int32)
> > > recordarr.foo[1:2]
> > > array([2], dtype=int32)
> > > recordarr[1].baz
> > > 'World'

numpy.rec.array可以将各种参数转换为记录数组，包括正常的结构化数组：

> > > arr = array([(1,2.,'Hello'),(2,3.,"World")], 
> > > ...             dtype=[('foo', 'i4'), ('bar', 'f4'), ('baz', 'S10')])
> > > recordarr = np.rec.array(arr)

numpy.rec模块提供了一些创建记录数组的其他便利函数，请参见record array creation routines。

可以使用适当的视图获得结构化数组的记录数组表示：

> > > arr = np.array([(1,2.,'Hello'),(2,3.,"World")], 
> > > ...                dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'a10')])
> > > recordarr = arr.view(dtype=dtype((np.record, arr.dtype)), 
> > > ...                      type=np.recarray)

为方便起见，以np.recarray类型查看ndarray将自动转换为np.record数据类型，因此dtype可以不在视图中：

> > > recordarr = arr.view(np.recarray)
> > > recordarr.dtype
> > > dtype((numpy.record, [('foo', '<i4'), ('bar', '<f4'), ('baz', 'S10')]))

要返回到一个普通的ndarray，dtype和type必须重置。以下视图是这样做的，考虑到recordarr不是结构化类型的不寻常情况：

> > > arr2 = recordarr.view(recordarr.dtype.fields or recordarr.dtype, np.ndarray)

通过索引或属性访问的记录数组字段将作为记录数组返回，如果字段具有结构化类型，则返回为纯数组。

> > > recordarr = np.rec.array([('Hello', (1,2)),("World", (3,4))], 
> > > ...                 dtype=[('foo', 'S6'),('bar', [('A', int), ('B', int)])])
> > > type(recordarr.foo)
> > > <type 'numpy.ndarray'>
> > > type(recordarr.bar)
> > > <class 'numpy.core.records.recarray'>

请注意，如果字段与ndarray属性具有相同的名称，则ndarray属性优先。这些字段将无法通过属性访问，但仍可通过索引访问。
