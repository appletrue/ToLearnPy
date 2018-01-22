# 数组创建

有多种方法来创建数组。

### numpy.array

使用array函数从常规Python列表或元组中创建数组。得到的数组的类型从序列中元素的类型推导出。

```python
import numpy as np
a = np.array([2,3,4])
b = np.array([1.2, 3.5, 5.1])
print(a.dtype)
print(b.dtype)
print(a.strides)
print(b.strides)
#输出结果如下：
int32
float64
(4,)
(8,)
```

#### 常见的错误在于用多个数字参数调用array，而不是提供单个数字列表作为参数。

```python
c = np.array(1,2,3,4)  ··  # ValueError: only 2 non-keyword arguments accepted
d = np.array([1,2,3,4])  
print(d.strides)
e = np.array(0)
#输出结果如下：
(4,)
0  #0维度数组
```

#### array将序列的序列转换成二维阵列，将序列的序列的序列转换成三维数组，等等。

>>> b = np.array([(1.5,2,3), (4,5,6)])
>>> b
array([[ 1.5,  2. ,  3. ],
       [ 4. ,  5. ,  6. ]])


#### 数组的类型也可以在创建时明确指定：

```python
c = np.array( [ [1,2], [3,4] ], dtype=complex )
print(c)
array([[ 1.+0.j,  2.+0.j],
       [ 3.+0.j,  4.+0.j]])
```

通常，数组的元素最初是未知的，但其大小是已知的。因此，NumPy提供了几个函数来创建具有初始占位符内容的数组。这就减少了数组增长的必要，因为数组增长的操作花费很大。(当长度不够时，会动态的选择并将原有数组复制到新的内存，继续增加数据。）

### zeros,ones,empty,random

函数zeros创建一个由0组成的数组，函数ones创建一个由1数组的数组，函数empty内容是随机的并且取决于存储器的状态。默认情况下，创建的数组的dtype为float64。

```python
import numpy as np
print(np.zeros( (3,4) ))
"""
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]"""
print(np.ones( (2,3,4), dtype=np.int16))             # dtype can also be specified
"""
[[[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]

 [[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]]"""
print(np.empty((2,3)))                                # uninitialized, output may vary
"""
[[  2.67276450e+185   1.69506143e+190   1.75184137e+190]
 [  9.48819320e+077   1.63730399e-306   3.81388253e+180]]
 """
print(np.random.random((2,3)))
"""输出结果
[[ 0.95233062  0.49687636  0.72729402]
 [ 0.29571206  0.72813817  0.26220836]]
 """
print(type(np.random.random((2,3))))		#<class 'numpy.ndarray'>
```

### numpy.arange

为了创建数字序列，NumPy提供类似于range的函数，返回数组而不是列表。

```python
import numpy as np
print(np.arange( 10, 30, 5 )) 		# it accepts float arguments
print(np.arange( 0, 2, 0.3 ) )
#输出结果如下：
[10 15 20 25]
[ 0.   0.3  0.6  0.9  1.2  1.5  1.8]
```

注意：当arange与浮点参数一起使用时，由于浮点数的精度是有限的，通常不可能预测获得的元素数量。出于这个原因，通常最好使用函数linspace，它接收我们想要的元素数量而不是步长作为参数：

```python
import numpy as np
from numpy import pi
print(np.linspace( 0, 2, 9 ))               # 9 numbers from 0 to 2,自动计算步长
x = np.linspace( 0, 2*pi, 3 )        # useful to evaluate function at lots of points
f = np.sin(x)
print(x,f)
#输出结果如下:
[ 0.    0.25  0.5   0.75  1.    1.25  1.5   1.75  2.  ]
[ 0.          3.14159265  6.28318531] [  0.00000000e+00   1.22464680e-16  -2.44929360e-16]
```

### numpy.fromfunction:	从给定函数创建一个数组
	
```python
import numpy as np

def f(x,y):
    return 2*x+y

b = np.fromfunction(f,(3,3),dtype=int)
print(b)
#输出结果如下:
#x,y的取值范围都在[0,2],各自取值得出以下
([[0, 1, 2],
  [2, 3, 4],
  [4, 5, 6]])
```

### eye和identity: 用于创建正方形矩阵，对角线元素都是1，其余为 0

```python
x = np.eye(2)
print(x)
#输出array
[[ 1.  0.]
 [ 0.  1.]]
 
y = np.eye(3)
print(y)
#输出array
     ([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

a = np.eye(3, k=1)
print(a)
#输出结果array
([[ 0.,  1.,  0.],
  [ 0.,  0.,  1.],
  [ 0.,  0.,  0.]])
  
b = np.eye(3, k=-1)
print(b)
#输出结果array
([[ 0.,  0.,  0.],
  [ 1.,  0.,  0.],
  [ 0.,  1.,  0.]])
c = np.eye(4,3)
print(c)
#输出结果array
([[ 1.,  0.,  0.],
  [ 0.,  1.,  0.],
  [ 0.,  0.,  1.],
  [ 0.,  0.,  0.]])
d = np.identity(3)
print(d)
#输出结果如下array
([[ 1.,  0.,  0.],
  [ 0.,  1.,  0.],
  [ 0.,  0.,  1.]])
```

### fromfile,tofile:从文件创建

使用数组的方法函数tofile可以方便地将数组中数据以二进制的格式写进文件。tofile输出的数据没有格式，因此用numpy.fromfile读回来的时候需要自己格式化数据:

```python
import numpy as np

a = np.arange(0,12)
a.shape = (3,4)
print(a)
#输出结果:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 
a.tofile("a.bin")       		 	#在目录下生成一个 a.bin 的文件
b = np.fromfile("a.bin", dtype=np.float) 	# 按照float类型读入数据
print(b) 					# 读入的数据是错误的
[  2.12199579e-314   6.36598737e-314   1.06099790e-313   1.48539705e-313   1.90979621e-313   2.33419537e-313]
print(a.dtype)		 			# 查看a的dtype 为 int32

b = np.fromfile("a.bin", dtype=np.int32) 	# 按照int32类型读入数据
print(b)					# 数据是一维的
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
b.shape = (3, 4) # 按照a的shape修改b的shape
print(b)			
#输出结果array
([[ 0,  1,  2,  3],
  [ 4,  5,  6,  7],
  [ 8,  9, 10, 11]])
```

### numpy.load和numpy.save

以NumPy专用的二进制类型保存数据，numpy.load和numpy.save这两个函数会自动处理元素类型和shape等信息，使用它们读写数组就方便多了，但是numpy.save输出的文件很难和其它语言编写的程序读入：

```python
import numpy as np
a = np.arange(0,12)
np.save("a.npy", a)
c = np.load( "a.npy" )

print(c)
[ 0  1  2  3  4  5  6  7  8  9 10 11]
```
 
## 数组创建常规方法库


### 零一数组
|方法|说明|
|---|---|
|empty（shape [，dtype，order]） |返回给定形状和类型的新数组，而不初始化条目|
|empty_like（a [，dtype，order，subok]） |返回具有与给定数组相同的形状和类型的新数组|
|eye（N [，M，k，dtype]） |返回一个2-D数组，其中一个在对角线上，零在其他地方|
|identity（n [，dtype]） |返回身份数组|
|ones（shape [，dtype，order]） |返回给定形状和类型的新数组，用数字填充|
|ones_like（a [，dtype，order，subok]） |返回与给定数组具有相同形状和类型的数组| 
|zeros（shape [，dtype，order]） |返回给定形状和类型的新数组，用零填充 |
|zeros_like（a [，dtype，order，subok]） |返回具有与给定数组相同的形状和类型的零数组 |
|full（shape，fill_value [，dtype，order]） |返回给定形状和类型的新数组，用fill_value填充 |
|full_like（a，fill_value [，dtype，order，subok]） |返回与给定数组相同形状和类型的完整数组 |


### 从已存在数据创建

|方法|说明|
|---|---|
|array(object[, dtype, copy, order, subok, ndmin]) |创建数组。|
|asarray(a[, dtype, order]) |将输入转换为数组。 |
|asanyarray(a[, dtype, order]) |将输入转换为ndarray，但传递ndarray子类。 |
|ascontiguousarray（a [，dtype]） |返回内存中的连续数组（C order）。 |
|asmatrix（data [，dtype]） |将输入解释为矩阵。 |
|copy（a [，order]） |返回给定对象的数组副本。 |
|frombuffer（buffer [，dtype，count，offset]） |将缓冲区解释为1维数组。 |
|fromfile（file [，dtype，count，sep]） |从文本或二进制文件中的数据构造数组。 |
|fromfunction（function，shape，\ * \ * kwargs） |通过在每个坐标上执行函数来构造数组。 |
|fromiter（iterable，dtype [，count]） |从可迭代对象创建新的1维数组。 |
|fromstring（string [，dtype，count，sep]） |根据字符串中的原始二进制或文本数据初始化的新1-D数组。 |
|loadtxt（fname [，dtype，comments，delimiter，...]） |从文本文件加载数据。 |


### 创建记录数组 (numpy.rec)

|方法|说明|
|---|---|
|core.records.array（obj [，dtype，shape，...]） |从各种各样的对象构造一个记录数组。 |
|core.records.fromarrays（arrayList [，dtype，...]） |从数组的（平面）列表创建一个记录数组 |
|core.records.fromrecords（recList [，dtype，...]） |从文本形式的记录列表创建一个recarray |
|core.records.fromstring（datastring [，dtype，...]） |从包含在中的二进制数据创建（只读）记录数组 |
|core.records.fromfile（fd [，dtype，shape，...]） |从二进制文件数据创建数组 |

### 创建字符数组 (numpy.char)

|方法|说明|
|---|---|
|core.defchararray.array（obj [，itemsize，...]） |创建chararray|
|core.defchararray.asarray（obj [，itemsize，...]） |将输入转换为chararray，只有在必要时才复制数据|


### 数值范围

|方法|说明|
|---|---|
|arange（[start，] stop [，step，] [，dtype]） |在给定间隔内返回均匀间隔的值。|
|linspace（start，stop [，num，endpoint，...]） |在指定的间隔内返回均匀间隔的数字。 |
|logspace（start，stop [，num，endpoint，base，...]） |返回以对数刻度均匀分布的数字。|
 
meshgrid（\ * xi，\ * \ * kwargs） 
从坐标向量返回坐标矩阵。 

mgrid nd_grid实例，返回密集的多维“网格网格”。 
ogrid nd_grid实例，返回一个打开的多维“meshgrid”。 


### 构建矩阵

|方法|说明|
|---|---|
|diag（v [，k]） |提取对角线或构造对角数组。  |
|diagflat（v [，k]）  |创建一个二维数组，将扁平输入作为对角线。  |
|tri（N [，M，k，dtype]）  |数组，其中一个在给定的对角线和在其他地方零。 |
|tril（m [，k]）  |数组的下三角形。 |
|triu（m [，k]）  |数组的上三角形。 |
|vander（x [，N，increasing]）  |生成Vandermonde矩阵。  |


### 矩阵类

|方法|说明|
|---|---|
|mat（data [，dtype]） |将输入解释为矩阵。 |
|bmat（obj [，ldict，gdict]） |从字符串，嵌套序列或数组构建一个矩阵对象。 |
