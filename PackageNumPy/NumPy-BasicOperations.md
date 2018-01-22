===================================================

NumPy-Basics-BasicOperations    
NumPy-Basics-Universal Functions

===================================================

# ndarray数组运算

NumPy提供了熟悉的数学函数，如sin，cos和exp。在NumPy中，这些被称为“通用函数”（ufunc）。在NumPy中，这些函数在数组上按元素级别操作，产生一个数组作为输出。

```python
B = np.arange(3)
print(B)				#array([0, 1, 2])
print(np.exp(B))		#array([ 1.        ,  2.71828183,  7.3890561 ])
print(np.sqrt(B))		#array([ 0.        ,  1.        ,  1.41421356])
C = np.array([2., -1., 4.])
print(np.add(B, C))		#array([ 2.,  0.,  6.])
```

数组上的算术运算符使用元素级别。将创建一个新数组并用结果填充。

```Python
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print(b)			#array([0, 1, 2, 3])
c = a-b
print(c)			#array([20, 29, 38, 47])
print(b**2)			#array([0, 1, 4, 9])
print(10*np.sin(a))	#array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
print(a<35)			#array([ True, True, False, False], dtype=bool)
```

在NumPy数组对应元素的操作，乘法运算符*的运算在NumPy数组中是元素级别的。可以使用点函数 `dot` 或方法执行矩阵乘积：

```python
A = np.array( [[1,1],
              [0,1]] )
B = np.array( [[2,0],
               [3,4]] )
print(A*B)                  # elementwise product
                            #array([[2, 0],
                                   [0, 4]])
print(A.dot(B))             # matrix product
                            # array([[5, 4],
                                     [3, 4]])
print(np.dot(A, B))         # another matrix product
                            # array([[5, 4],
                                     [3, 4]])
```

某些操作，如 `+=` 、 `*=`, 用于修改现有数组，而不是创建一个新数组。

```python
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
a *= 3
print(a)
                  #array([[3, 3, 3],
                          [3, 3, 3]])
b += a
print(b)
                  #array([[ 3.417022  ,  3.72032449,  3.00011437],
                         [ 3.30233257,  3.14675589,  3.09233859]])
a += b                  # b is not automatically converted to integer type
Traceback (most recent call last):
  ...
TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
```

当使用不同类型的数组操作时，结果数组的类型对应于更一般或更精确的数组（称为向上转换的行为）。

```python
a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)				#'float64'
c = a+b
print(c)						#array([ 1.        ,  2.57079633,  4.14159265])
print(c.dtype.name)				#'float64'
d = np.exp(c*1j)
print(d)
#输出：
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
print(d.dtype.name)				#'complex128'
```

许多一元运算，如计算数组中的所有元素的总和，是实施的 `ndarray` 类方法。

```python
a = np.random.random((2,3))
print(a)
#输出结果：
array([[ 0.18626021,  0.34556073,  0.39676747],
       [ 0.53881673,  0.41919451,  0.6852195 ]])
print(a.sum())			#2.5718191614547998
print(a.min())			#0.1862602113776709
print(a.max())			#0.6852195003967595
```

默认情况下，这些操作应用于数组，就像它是一个数字列表，而不管它的形状如何。但是，通过指定轴 `axis` 参数，您可以沿着数组指定的轴应用操作：

```python
b = np.arange(12).reshape(3,4)
print(b)
#array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
print(b.sum(axis=0))        # sum of each column
							# array([12, 15, 18, 21])
print(b.min(axis=1))        # min of each row
							# array([0, 4, 8])
print(b.cumsum(axis=1))     # cumulative sum along each row
                            # array([[ 0,  1,  3,  6],
                                     [ 4,  9, 15, 22],
                                     [ 8, 17, 27, 38]])
```


## 数学函数:Mathematical functions

### 三角函数:Trigonometric functions

| 方法                | 说明         |
| ------------------ | ------------ |
|sin（x [，out]）| 三角正弦，元素。 |
|cos（x [，out]）| 元素方面。 |
|tan（x [，out]） |逐元素计算切线。 |
|arcsin（x [，out]）| 反正弦，元素。 |
|arccos（x [，out]）| 三角反余弦，元素方式。| 
|arctan（x [，out]） |三角反正切，元素。 |
|hypot（x1，x2 [，out]） |给定直角三角形的“腿”，返回其斜边。 |
|arctan2（x1，x2 [，out]） |x1/x2的元素平方倒圆切线正确选择象限。 |
|degrees（x [，out]） |将角度从弧度转换为度。 |
|radians（x [，out]）| 将角度从度转换为弧度。 |
|unwrap（p [，discont，axis]） |通过将值之间的delta改为2 * pi补码来展开。 |
|deg2rad（x [，out]）| 将角度从度转换为弧度。 |
|rad2deg（x [，out]） |将角度从弧度转换为度。 |

### 双曲函数:Hyperbolic functions

| 方法                | 说明         |
| ------------------ | ------------ |
|sinh（x [，out]） |双曲正弦，元素。 |
|cosh（x [，out]） |双曲余弦，元素。 |
|tanh(x[, out]) |逐元素计算双曲正切 |
|arcsinh（x [，out]）|逆双曲正弦元。 |
|arccosh（x [，out]）| 逆双曲余弦，元素方式。 |
|arctanh（x [，out]） |逆双曲正切元素。 |

### 取整:Rounding

| 方法                | 说明         |
| ------------------ | ------------ |
|around（a [，decimals，out]） |均匀到给定的小数位数。 |
|round_（a [，decimals，out]）| 将数组舍入到给定的小数位数。| 
|rint（x [，out]） |数组的圆形元素到最接近的整数。 |
|fix（x [，y]） |向零舍入到最接近的整数。 |
|floor（x [，out]） |逐元素地返回输入的底。 |
|ceil（x [，out]） |元素方式返回输入的上限。 |
|trunc（x [，out]）| 按元素方式返回输入的截断值。 |

### Sums, products, differences

| 方法                | 说明         |
| ------------------ | ------------ |
|prod（a [，axis，dtype，out，keepdims]） |返回给定轴上的数组元素的乘积。| 
|sum（a [，axis，dtype，out，keepdims]） |给定轴上的数组元素的总和。 |
|nanprod（a [，axis，dtype，out，keepdims]） |返回数组元素在给定轴上的处理非数字（NaN）为零的乘积。 |
|nansum（a [，axis，dtype，out，keepdims]） |返回在给定轴上处理非数字（NaN）为零的数组元素的总和。| 
|cumprod（a [，axis，dtype，out]） |返回沿给定轴的元素的累积积。 |
|cumsum（a [，axis，dtype，out]） |返回沿给定轴的元素的累积和。 |
|nancumprod  ||
|nancumsum  ||
|diff（a [，n，axis]）| 计算沿给定轴的第n个离散差分。 |
|ediff1d（ary [，to_end，to_begin]） |数组的连续元素之间的差异。| 
|gradient（f，\ * varargs，\ * \ * kwargs） |返回N维数组的梯度。 |
|cross（a，b [，axisa，axisb，axisc，axis]） |返回两个（数组）向量的叉积。 |
|trapz（y [，x，dx，axis]） |使用复合梯形法则沿给定轴进行积分。 |

### 指数和对数:Exponents and logarithms

| 方法                | 说明         |
| ------------------ | ------------ |
|exp（x [，out]） |计算输入数组中所有元素的指数。 |
|expm1（x [，out]）| 对数组中的所有元素计算exp（x） -  1  |
|exp2（x [，out]）| 对于输入数组中的所有p，计算2 ** p。 |
|log（x [，out]）| 自然对数，逐元素。 |
|log10（x [，out]）| 以元素为单位返回输入数组的基数10的对数。 |
|log2（x [，out]）| x的基础2对数。 |
|log1p（x [，out]） |返回一个加自然对数的输入数组，元素。|
|logaddexp（x1，x2 [，out]）| 输入的求和的对数。 |
|logaddexp2（x1，x2 [，out]） |以2为底的输入的乘方和的对数。 |

### 其他特殊函数:Other special functions

| 方法                | 说明         |
| ------------------ | ------------ |
|i0（x）| 修改Bessel函数的第一类，顺序为0|
|sinc（x） |返回sinc函数。 |

### 浮点常规:Floating point routines

| 方法                | 说明         |
| ------------------ | ------------ |
|signbit（x [，out]） |以元素为单位返回True，其中signbit已设置（小于零）。 |
|copysign（x1，x2 [，out]） |按照元素方式将x1的符号更改为x2的符号。| 
|frexp（x [，out1，out2]）| 将x的元素分解为尾数和二进制指数。 |
|ldexp（x1，x2 [，out]） |元素方式返回x1 * 2 ** x2。| 

### 算数运算:Arithmetic operations

| 方法                | 说明         |
| ------------------ | ------------ |
|add（x1，x2 [，out]） |按元素添加参数。 |
|reciprocal（x [，out]） |元素方式返回参数的倒数。| 
|negative（x [，out]） |数值负，元素。 |
|multiply（x1，x2 [，out]） |逐元素乘法参数。| 
|divide（x1，x2 [，out]）| 逐元素分割参数。 |
|power（x1，x2 [，out]） |第一个数组元素从第二个数组提升到权力，逐元素。 |
|subtract（x1，x2 [，out]） |按元素方式减去参数。 |
|true_divide（x1，x2 [，out]）| 按元素方式返回输入的真正除法。 |
|floor_divide（x1，x2 [，out]） |返回小于或等于输入的除法的最大整数。 |
|fmod（x1，x2 [，out]） |返回除法的元素余项。 |
|mod（x1，x2 [，out]） |返回元素的除法余数。 |
|modf（x [，out1，out2]） |以元素方式返回数组的小数和整数部分。| 
|remainder（x1，x2 [，out]）| 返回元素的除法余数。 |

### 复数处理:Handling complex numbers

| 函数                | 说明         |
| ------------------ | ------------ |
|angle（z [，deg]）| 返回复参数的角度。 |
|real（val）       |返回数组的元素的实数部分。 |
|imag（val）        |返回数组的元素的虚部。 |
|conj（x [，out]） |按元素方式返回复共轭。 |

### 杂项:Miscellaneous

| 函数                | 说明         |
| ------------------ | ------------ |
|convolve（a，v [，mode]） |返回两个一维序列的离散，线性卷积。 |
|clip（a，a_min，a_max [，out]） |剪辑（限制）数组中的值。 |
|sqrt（x [，out]） |按元素方式返回数组的正平方根。 |
|cbrt（x [，out]） |以元素方式返回数组的多维数据集根。 |
|square（x [，out]） |返回输入的元素平方。 |
|absolute（x [，out]）| 逐个计算绝对值。 |
|fabs（x [，out]） |按元素计算绝对值。 |
|sign（x [，out]） |返回数字符号的逐元素指示。 |
|maximum（x1，x2 [，out]） |数组元素的元素最大值。 |
|minimum（x1，x2 [，out]） |元素最小的数组元素。 |
|fmax（x1，x2 [，out]） |数组元素的元素最大值。| 
|fmin（x1，x2 [，out]） |元素最小的数组元素。 |
|nan_to_num（x） |用零和inf替换nan为有限数。 |
|real_if_close（a [，tol]） |如果复杂的输入返回一个真实的数组，如果复杂的零件接近零。 |
|interp（x，xp，fp [，left，right，period]） |一维线性插值。 |


## 排序：Sorting

| 方法                | 说明         |
| ------------------ | ------------ |
|sort（a [，axis，kind，order]） |返回数组的排序副本。| 
|lexsort（keys [，axis]） |使用键序列执行间接排序。 |
|argsort（a [，axis，kind，order]） |返回将数组分类的索引。| 
|ndarray.sort（[axis，kind，order]）| 就地对数组进行排序。| 
|msort（a）| 返回沿第一个轴排序的数组的副本。 |
|sort_complex（a） |使用实部，然后是虚部对复数数组进行排序。| 
|partition（a，kth [，axis，kind，order]） |返回数组的分区副本。 |
|argpartition（a，kth [，axis，kind，order]） |使用种关键字指定的算法沿给定轴执行间接分区。 |

排序举例：

使用sort对数组/数组某一维度进行就地排序（会修改数组本身）

.sort：就地排序
```python
x = np.array([[1,6,2],[6,1,3],[1,5,2]])
x.sort(axis=1) 
print(x)          #array([[1 2 6][1 3 6] [1 2 5]])
```

非就地排序：numpy.sort()可产生数组的副本

## 搜索:Searching

| 方法                | 说明         |
| ------------------ | ------------ |
|argmax（a [，axis，out]） |返回沿轴的最大值的索引。 |
|nanargmax（a [，axis]） 	|返回指定轴中忽略NaNs的最大值的索引。| 
|argmin（a [，axis，out]） |返回沿轴的最小值的索引。 |
|nanargmin（a [，axis]）	 |返回指定轴中忽略NaN的最小值的索引。 |
|argwhere（a）			    |找到非零的数组元素的索引，按元素分组。 |
|nonzero（a） 			    |返回非零元素的索引。 |
|flatnonzero（a）			    |在a的扁平版本中返回非零的索引。 |
|**where（条件，[x，y]）** 		 |根据条件，从x或y返回元素。 |
|searchsorted（a，v [，side，sorter]） |查找要插入元素以维持顺序的索引。 |
|extract（condition，arr）		   |返回满足某些条件的数组的元素。| 

例子：
#### where函数

np.where(condition, x, y)

condition:为一个布尔值或数组；
x,y:可以是标量也可以是数组。condition为True，取x；否则取y；


```python
cond = np.array([True,False,True,False])
x = np.where(cond,-2,2)
print(x)                #array([-2,  2, -2,  2])

cond = np.array([1,2,3,4])
x = np.where(cond>2,-2,2)
print(x)                #array([ 2,  2, -2, -2])

y1 = np.array([-1,-2,-3,-4])
y2 = np.array([1,2,3,4])
x = np.where(cond>2,y1,y2) # 长度须匹配
print(x)                   #array([ 1,  2, -3, -4])
```

#### where函数的嵌套使用

```python
y1 = np.array([-1,-2,-3,-4,-5,-6])
y2 = np.array([1,2,3,4,5,6])
y3 = np.zeros(6)
cond = np.array([1,2,3,4,5,6])
x = np.where(cond>5,y3,np.where(cond>2,y1,y2))
print(x)             # array([ 1.,  2., -3., -4., -5.,  0.])
```

## 逻辑函数

### 真值测试：Truth value testing

| 函数                | 说明         |
| ------------------ | ------------ |
|all（a [，axis，out，keepdims]）| 测试沿给定轴的所有数组元素是否为True。 |
|any（a [，axis，out，keepdims]） |测试沿给定轴的任何数组元素是否为True。 |

### 数组内容：Array contents

| 函数                | 说明         |
| ------------------ | ------------ |
|isfinite（x [，out]） |测试元素的有限性（不是无穷大或不是数字）|。 
|isinf（x [，out]） |对于正或负无穷大测试元素。 |
|isnan（x [，out]） |测试元素方面的NaN和返回结果作为一个布尔数组。 |
|isneginf（x [，y]） |测试元素为负无穷大，返回结果为bool数组。 |
|isposinf（x [，y]） |测试元素为正无穷大，返回结果为bool数组。 |

### 数组类型测试：Array type testing

| 函数                | 说明         |
| ------------------ | ------------ |
|iscomplex（x）| 返回bool数组，其中如果输入元素很复杂，则返回True。 |
|iscomplexobj（x） |检查复杂类型或复数的数组。 |
|isfortran（a） |如果数组是Fortran连续但不是 C连续，则返回True。 |
|isreal（x） |返回bool数组，其中如果输入元素是实数，则返回True。| 
|isrealobj（x） |如果x不是复数类型或复数数组，则返回True。 |
|isscalar（num） |如果num的类型是标量类型，则返回True。 |

### 逻辑运算：Logical operations

| 函数                | 说明         |
| ------------------ | ------------ |
|logical_and（x1，x2 [，out]） |逐元素计算x1和x2的真值。 \|
|logical_or（x1，x2 [，out]） |逐元素计算x1或x2的真值。 |
|logical_not（x [，out]） |逐元素计算NOT x的真值。 |
|logical_xor（x1，x2 [，out]） |按元素方式计算x1 XOR x2的真值。 |

### 比较

| 函数                | 说明         |
| ------------------ | ------------ |
|allclose(a, b[, rtol, atol, equal_nan]) |如果两个数组在元素级别在公差内相等，则返回True。| 
|isclose（a，b [，rtol，atol，equal_nan]） |返回一个布尔数组，其中两个数组在容差内在元素方面相等。| 
|array_equal（a1，a2） |如果两个数组具有相同的形状和元素，则为True，否则为False。 |
|array_equiv（a1，a2） |返回True如果输入数组的形状一致，所有元素相等。 |
|greater（x1，x2 [，out]） |逐元素地返回（x1> x2）的真值。 |
|greater_equal（x1，x2 [，out]） |逐元素地返回（x1> = x2）的真值。 |
|less（x1，x2 [，out]） |返回（x1的真值 \|
|less_equal（x1，x2 [，out]） |返回（x1 =）的真值 |
|equal（x1，x2 [，out]） |元素方式返回（x1 == x2）。 |
|not_equal（x1，x2 [，out]） |元素方式返回（x1！= x2）。 |
