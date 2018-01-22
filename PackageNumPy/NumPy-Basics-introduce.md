# numpy 快速入门学习&具体操作

------[参考地址：](https://docs.scipy.org/doc/numpy/user/quickstart.html) 

numpy 用于对矩阵matric的操作，一般会结合Pandas一同import 

- np.lookfor('create array')  #查找命令
 
 
## 数组概念

NumPy的主要对象是同类型的多维数组。它是一张表，所有元素（通常是数字）的类型都相同，并通过正整数元组索引。在NumPy中，维度称为轴。轴的数目为rank。

例如，3D空间中的点的坐标[1, 2, 1]是rank为1的数组，因为它具有一个轴（axis）。该轴的长度为3。
在下图所示的示例中，数组的rank为2（它是2维的）。第一维度（轴）的长度为2，第二维度的长度为3。

[[ 1., 0., 0.],
 [ 0., 1., 2.]]

NumPy的数组的类称为ndarray。别名为array。
请注意，numpy.array与标准Python库的类array.array不同，后者仅处理一维数组并提供较少的功能。

🌹注意： numpy 中数组array和矩阵matric的区别：  

NumPy函数库中存在两种不同的数据类型（矩阵matrix和数组array），都可以用于处理行列表示的数字元素。

看起来相似，但当执行同样的数学运算时，有可能会得到不同的运算结果。如MLIA 中的实例：
```python
import numpy as np  #将NumPy函数库中的所有模块引入到当前命名空间 
arrayX = np.random.rand(2,2)   
print(arrayX)   
randMatric = np.mat(arrayX) #将数组array转换成矩阵matrix  
print(randMatric)   
invRandMatric = randMatric.I #.I操作实现了逆矩阵的运算   
print(invRandMatric)   
myEye = randMatric*invRandMatric #矩阵与其逆矩阵相乘   
print(myEye) print(myEye-np.eye(2)) #np.eye()创建4X4的单位矩阵

输出结果为：

> [[ 0.06837544  0.61489627]  
 [ 0.32350553  0.79551299]]  
[[ 0.06837544  0.61489627]  
 [ 0.32350553  0.79551299]]  
[[-5.50418341  4.25448969]  
 [ 2.23834657 -0.47309214]]  
[[  1.00000000e+00  -2.62120939e-18]  
 [  4.98500312e-17   1.00000000e+00]]  
[[  0.00000000e+00  -2.62120939e-18]  
 [  4.98500312e-17   2.22044605e-16]]
```

## ndarray对象数组属性

### 数组的轴 ndarray.ndim

数组的轴（维度，dimensionality）的个数。在Python世界中，维度的数量被称为rank。

```python
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print(x)
print(x.ndim)

#输出结果如下： 
array([[1, 2, 3],
       [4, 5, 6]])
2
```

### 数组的维度 ndarray.shape

数组的维度，是一个整数的元组，表示每个维度中数组的大小。

对于具有n行和m列的矩阵，shape将是(n,m)。因此，shape元组的长度就是rank或维度的个数ndim。

```python
....
print(x.shape)
#输出结果如下：
 (2, 3)
```
### 数组元素的总数 ndarray.size

数组元素的总数。这等于shape的元素的乘积。

示例：
```python
....
print(x.size)	 # 6
```

### 数组中每个元素的字节大小. ndarray.itemsize

例如，元素为float64类型的数组的itemsize为8（=64/8），而complex32类型的数组的comitemsize为4（=32/8）。它等于ndarray.dtype.itemsize。

```python
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
y = np.array([1.,2,3])
z = np.array([1.,2,3],dtype=np.int64)
print(x.dtype)
print(x.itemsize)
print(y.dtype)
print(y.itemsize)
print(z.dtype)
print(z.itemsize)
# 输出结果如下：
int32
4
float64
8
int64
8
```

### 数组步长幅度  ndarray.strides

```python
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print(x.strides)
#输出结果如下：
(12, 4) 		#一行3个元素，每个大小4字节
y = np.array([[1,2],[3,4],[5,6]])
print(y.strides)
#输出结果如下：
(8, 4) 			#一行2个元素，每个大小8字节
z = np.array([1.,2,3],dtype=np.int64)
print(z.strides)
#输出结果如下：
(8,)			#只有1行，每个大小8字节
```
	
### ndarray.data

该缓冲区包含数组的实际元素。通常，我们不需要使用此属性，因为我们将使用索引访问数组中的元素。

### 存放数组自身的相关信息：ndarray.flags

————contiguous：连续的

```python
x = np.array([[1,2,3],[4,5,6]])
print(x.flags)
print(x.flags.owndata)
print(x.flags.writeable)
#输出结果如下：
  C_CONTIGUOUS : True#
  F_CONTIGUOUS : False
  OWNDATA : True			#自身数据（区别指针指向）
  WRITEABLE : True			#可写
  ALIGNED : True 			#是否对齐
  UPDATEIFCOPY : False			#复制是否更新		
True
True
```

### 数组中元素类型 ndarray.dtype

Numpy支持比Python更多种类的数值类型。此部分显示了哪些可用的，以及如何修改数组的数据类型。

描述数组中元素类型的对象。可以使用标准Python类型创建或指定dtype。另外NumPy提供了自己的类型。

例如numpy.int32、numpy.int16和numpy.float64。

```python
print(x.dtype)		# int32
dtype('int32')
#注意以下类型转换
y = np.array([1.,2,3])	
print(y)
print(y.dtype)		# dtype('float64')
#输出结果如下：
[ 1.  2.  3.]
float64
```

### NumPy中的基本数据类型取值范围

|名称| 描述|
|---|---|
|bool 		|用一个Bit存储的布尔类型（True或False） |
|inti 		|由所在平台决定其大小的整数（一般为int32或int64） |
|int8 		|一个字节大小，-128 至 127 |
|int16 		|整数，-32768 至 32767 |
|int32 		|整数，-2 ** 31 至 2 ** 32 -1 |
|int64 		|整数，-2 ** 63 至 2 ** 63 - 1 |
|uint8 		|无符号整数，0 至 255 |
|uint16 	|无符号整数，0 至 65535 |
|uint32 	|无符号整数，0 至 2 ** 32 - 1 |
|uint64  	|无符号整数，0 至 2 ** 64 - 1 |
|float16 	|半精度浮点数：16位，正负号1位，指数5位，精度10位 |
|float32 	|单精度浮点数：32位，正负号1位，指数8位，精度23位 |
|float64或float 	|双精度浮点数：64位，正负号1位，指数11位，精度52位 |
|complex64 	|复数，分别用两个32位浮点数表示实部和虚部 |
|complex128或complex |复数，分别用两个64位浮点数表示实部和虚部 |

### 类型名称使用规则

Numpy数值类型是dtype（data-type）对象的实例，每个类型具有唯一的特征。使用方式有：

#### 直接使用 

```python
np.array([1],dtype=complex).dtype
dtype('complex128')
```

#### 添加np包名前缀，避免冲突

在你使用下面的语句导入NumPy后,这些类型可以用np.bool_、np.float32等方式访问

```python
import numpy as np

np.array([1],dtype=np.complex).dtype		# dtype('complex128')
```

#### 使用字符简称


```python
print(np.array([1],dtype='c16').dtype)		#dtype('complex128')
```
简称前可以加` '|','<','>'`,分别表示：

`| `: 忽视字节顺序

`<` : 低位字节在前,小端 little endian

`> `: 高位字节在前,大端，big endian

例如:a = 0x12345678

- 小端：
 00	01	02	03
 
|78	|56 	|34 	|12

- 大端：
 00	01	02	03
 
|12|	34 |	56 |	78

>>> np.array([1],dtype='<i8').dtype

有关类型名称及简称，具体参考下表：

|np.类型名	|  对应于别的语言的类型  |字符简称（类型代码）|
|----------|---------------------|-----------------|
|**Booleans**   |--|	---|
|np.bool_ |Python bool |'?' |
|np.bool8 |8 bit bool  ||       	
|**Int** |       |	|
|np.byte  |	C char 	| 'b' |
|np.short |	C short |'h' |
|np.intc  |	C int   | 'i'   #int32 |
|np.int_ |	|Python int |'l' |
|np.longlong |	C long long | 'q' |
|np.intp 	|用作指针?? |'p' |
|np.int8	|特定长度	|'i1'|
|np.int16	|特定长度	|'i2'|
|np.int32	|特定长度	|'i4'|
|np.int64 	|特定长度   |'i8'| 	
|**Unsigned Int**||| 
|np.ubyte |C unsigned char |'B' |
|np.ushort |C unsigned short |'H' |
|np.uintc |C unsigned int |'I' |
|np.uint_ |Python unsigned int 	|'L' |
|np.ulonglong 	|C unsigned long long 	|'Q' |
|np.uintp |用作指针?? |'P' |
|np.uint8|特定长度	|'u1'|
|np.uint16|特定长度	|'u2'|
|np.uint32|特定长度	|'u4'|
|np.uint64 |特定长度 |'u8'|
|**Float** |||
|np.single |C float |'f' |
|np.double |C double  ||
|np.float_ |Python float|'d' |
|np.longfloat|C long float |'g' |
|np.float32|特定长度|'f4'|
|np.float64|特定长度|'f8'|
|np.float96|依赖于平台|
|np.float128 |依赖于平台|'f16'|
|**Complex(复数)** |||
|np.csingle   ||'F' |
|np.complex_ |	Python complex 	|'D' 
|np.clongfloat |特定长度|'G' 
|np.complex64	|特定长度|'c8'
|np.complex128	|特定长度|'c16'
|np.complex192	|依赖于平台||
|np.complex256| 依赖于平台|'c32'|
|**Any Python Object** |||
|np.object_ |保存的实际是引用 |'O' |
|np.str_ |Python str |'S#' # = number #控制每个str长度 |
|np.unicode_ 	|Python unicode |'U#' |
|void 	||	'V#' |


### 类型转换：

```python
import numpy as np

x = np.array([1,2,3],dtype = np.float64)
print(x)		#[ 1.  2.  3.]
print(x.dtype)          #float64
y = x.astype(np.int64)	#astype()不能直接作用于原实例
print(y)           	#[1 2 3]
print(y.dtype)      	#int64	
```
