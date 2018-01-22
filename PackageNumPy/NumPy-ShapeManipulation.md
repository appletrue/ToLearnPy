# 更改数组的形状

数组具有由沿着每个轴的元素数量给出的形状：**np.floor 向下取整， np.ceil 向上取整**

```python
import numpy as np

a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.shape)
#输出结果:
[[ 6.  1.  4.  4.]
 [ 6.  5.  2.  3.]
 [ 6.  1.  8.  0.]]
(3, 4)
```

可以使用各种命令更改数组的形状。请注意，以下三个命令都**返回修改的数组，但不更改原始数组**：

```python
import numpy as np

a = np.floor(10*np.random.random((3,4)))

print(a.ravel())	# [ 9.  2.  7.  1.  2.  9.  2.  3.  3.  7.  6.  6.]
print(a)
      [[ 9.  2.  7.  1.]
       [ 2.  9.  2.  3.]
       [ 3.  7.  6.  6.]]
print(a.reshape(6,2))
      [[ 9.  2.]
       [ 7.  1.]
       [ 2.  9.]
       [ 2.  3.]
       [ 3.  7.]
       [ 6.  6.]]
print(a.T)
      [[ 9.  2.  3.]
       [ 2.  9.  7.]
       [ 7.  2.  6.]
       [ 1.  3.  6.]]
print(a.T.shape)			#(4, 3) 
```

由ravel()产生的数组中元素的顺序通常是“C风格”，也就是说，最右边的索引“改变最快”，所以[0,0]之后的元素是[0,1] 。

如果数组被重塑成某种其他形状，则该数组也被视为“C风格”。NumPy通常创建按此顺序存储的数组，因此ravel()通常不需要复制其参数，但如果数组是通过对另一个数组进行切片或使用不寻常的选项创建的，则可能需要复制。

还可以使用可选参数来指示函数ravel()和reshape()，以使用FORTRAN式数组，其中最左侧的索引改变最快。

reshape函数返回其修改形状的参数，而ndarray.resize方法修改数组本身：???

```python
import numpy as np

a = np.floor(10*np.random.random((3,4)))

b = a.resize((2,6))
print(a)
      [[ 7.  0.  6.  6.  1.  2.]
       [ 6.  8.  2.  0.  5.  2.]]
print(b)		#None
```

如果在reshape操作中将维度指定为-1，则会自动计算其他维度：

```python
import numpy as np

a = np.floor(10*np.random.random((3,4)))

l = a.reshape(3,-1)         #将维度指定为-1，则会自动计算其他维度
k = np.arange(8).reshape(2,2,2)
m = k.swapaxes(0,1) # 将第一个轴和第二个轴交换 my[z] = kx[z]
n = k.transpose((1,2,0)) # my[x] = kx[z]
print(l)
      [[ 1.  0.  0.  4.]
       [ 9.  0.  4.  9.]
       [ 5.  3.  3.  8.]]
print(k)
      [[[0 1]
        [2 3]]   #----1
       [[4 5]    #----2
        [6 7]]]
print(m)
      [[[0 1]
        [4 5]]  #----1
       [[2 3]	#----2
        [6 7]]]
print(n)
        [[[0 4]
          [1 5]]
         [[2 6]
          [3 7]]]
```

轴交换另见:

ndarray.shape，reshape，resize，ravel

### 将不同数组堆叠在一起

- vstack&hstack: 几个数组可以沿不同的轴堆叠在一起：

```python
import numpy as np

a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print(a)
      [[ 3.  5.]
       [ 5.  9.]]
print(b)
      [[ 6.  3.]
       [ 8.  5.]]
print(np.vstack((a,b)))
      [[ 3.  5.]
       [ 5.  9.]
       [ 6.  3.]
       [ 8.  5.]]
print(np.hstack((a,b)))
      [[ 3.  5.  6.  3.]
       [ 5.  9.  8.  5.]]
```

函数column_stack将1D数组作为列堆叠到2D数组中。它等同于仅用于2D数组的hstack：

```python
import numpy as np
from numpy import newaxis

a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print(a)
[[ 3.  2.]
 [ 7.  0.]]
print(b)
[[ 5.  9.]
 [ 8.  7.]]
print(a[:,newaxis]) 

print(np.column_stack((a[:,newaxis],b[:,newaxis])))
[[[ 3.  2.]]
 [[ 7.  0.]]]
print(np.hstack((a[:,newaxis],b[:,newaxis])))  # the result is the same
[[[ 3.  2.]
  [ 5.  9.]]
 [[ 7.  0.]
  [ 8.  7.]]]
[[[ 3.  2.]
  [ 5.  9.]]
 [[ 7.  0.]
  [ 8.  7.]]]
print(np.vstack((a[:,newaxis],b[:,newaxis])))
[[[ 3.  2.]]
 [[ 7.  0.]]
 [[ 5.  9.]]
 [[ 8.  7.]]]
```

另一方面，对于任何输入数组，函数row_stack等效于vstack。一般来说，对于具有两个以上维度的数组，hstack沿第二轴堆叠，vstack沿第一轴堆叠，concatenate允许一个可选参数，给出串接应该发生的轴。

注意::在复杂情况下，r_和c_可用于通过沿一个轴堆叠数字来创建数组。它们允许使用范围文字（“：”）

> > > 

```python
print(np.r_[1:4,0,4])      #array([1, 2, 3, 0, 4])
print(np.c_[1:4])
#输出结果：
array([[1],
      [2],
      [3]])
```

当以数组作为参数使用时，r_和c_类似于其默认行为中的vstack和hstack，但是允许一个可选参数给出要沿其连接的轴的编号。

另见: hstack，vstack，column_stack，concatenate，c_，r_

### 将一个数组分成几个较小的数组

使用hsplit，可以沿其水平轴拆分数组，通过指定要返回的均匀划分的数组数量，或通过指定要在其后进行划分的列：

```python
a = np.floor(10*np.random.random((2,12)))
print(np.hsplit(a,3))   # Split a into 3
print(np.hsplit(a,(3,4)))   # Split a after the third and the fourth column
```

vsplit沿垂直轴分割，array_split允许指定沿哪个轴分割。

### 平铺和重复

```python
x = np.array([[1,2],[3,4]])
x.repeat(2,axis=0) # 按行重复 
x.repeat(2) # 按元素重复 
x.repeat(2,axis=1) # 按列重复
np.tile(x,2) 			# tile瓦片
np.tile(x, (3, 2))  # 指定从低维到高维依次复制的次数。 
```

### Changing array shape:改变数组阵型

| 方法                | 说明         |
| ------------------ | ------------ |
|reshape（a，newshape [，order]）| 为数组提供新形状，而不更改其数据。 |
|ravel（a [，order]）| 返回一个连续的扁平数组。 |
|ndarray.flat |数组上的1-D迭代器。 |
|ndarray.flatten（[order]） |将折叠的数组的副本返回到一个维度。 |

### Transpose-like operations：转置操作

| 方法                | 说明         |
| ------------------ | ------------ |
|moveaxis（a，源，目标） |将数组的轴移动到新位置。 |
|rollaxis（a，axis [，start]） |向后滚动指定的轴，直到它位于给定位置。 |
|swapaxes（a，axis1，axis2）| 交换数组的两个轴。 |
|ndarray.T |与self.transpose()相同，除非self是self.ndim返回 |
|transpose（a [，axes]） |允许数组的尺寸。 |

### Changing number of dimensions：改变数组的维度

| 方法                | 说明         |
| ------------------ | ------------ |
|atleast_1d（\ * arys） |将输入转换为具有至少一个维度的数组。| 
|atleast_2d（\ * arys） |将输入视为具有至少两个维度的数组。| 
|atleast_3d（\ * arys） |将输入视为至少包含三个维度的数组。| 
|broadcast |产生模仿广播的对象。 |
|broadcast_to（array，shape [，subbok]） |将数组广播到新形状。 |
|broadcast_arrays（\ * args，\ * \ * kwargs） |相互之间广播任意数量的数组。 |
|expand_dims（a，axis） |展开数组的形状。 |
|squeeze（a [，axis]） |从数组的形状中删除单维条目。| 

### Changing kind of array：改变数组类型

| 方法                | 说明         |
| ------------------ | ------------ |
|asarray（a [，dtype，order]） |将输入转换为数组。| 
|asanyarray（a [，dtype，order]）| 将输入转换为ndarray，但传递ndarray子类。| 
|asmatrix（data [，dtype]）| 将输入解释为矩阵。 |
|asfarray（a [，dtype]） |返回一个转换为float类型的数组。| 
|asfortranarray（a [，dtype]） |返回在Fortran中排列的数组在内存中的顺序。| 
|ascontiguousarray（a [，dtype]） |返回内存中的连续数组（C order）。 |
|asarray_chkfinite（a [，dtype，order]） |将输入转换为数组，检查NaN或Infs。 |
|asscalar（a） |将大小为1的数组转换为其标量等效值。 |
|require（a [，dtype，requirements]） |返回满足要求的所提供类型的数组。| 

### Joining arrays：数据连接

| 方法                | 说明         |
| ------------------ | ------------ |
|concatenate（（a1，a2，...）[，axis]） |沿现有轴连接数组序列。 |
|stack（arrays [，axis]） |沿着新轴连接数组的序列。 |
|column_stack（tup） |将1-D数组作为列堆叠到2-D数组中。 |
|dstack（tup） |按照深度顺序（沿第三轴）堆叠数组。 |
|hstack（tup） |水平（按列顺序）堆叠数组。 |
|vstack（tup）| 垂直（按行）顺序堆叠数组。 |

### Splitting arrays：分割数组

| 方法                | 说明         |
| ------------------ | ------------ |
|split（ary，indices_or_sections [，axis]） |将数组拆分为多个子数组。 |
|array_split（ary，indices_or_sections [，axis]） |将数组拆分为多个子数组。| 
|dsplit（ary，indices_or_sections） |将数组沿着第3轴（深度）拆分成多个子数组。| 
|hsplit（ary，indices_or_sections） |将数组水平（逐列）拆分为多个子数组。 |
|vsplit（ary，indices_or_sections） |垂直（行方向）将数组拆分成多个子数组。| 

### Tiling arrays：瓦片数组

| 方法                | 说明         |
| ------------------ | ------------ |
|tile（A，reps） |通过重复A由reps指定的次数构造数组。| 
|repeat（a，重复[，轴]）| 重复数组的元素。 |

### Adding and removing elements：增加和删除数组数据

| 方法                | 说明         |
| ------------------ | ------------ |
|delete（arr，obj [，axis]） |返回具有沿着轴删除的子数组的新数组。 |
|insert（arr，obj，values [，axis]） |在给定的索引之前沿给定轴插入值。 |
|append（arr，values [，axis]） |将值附加到数组的末尾。 |
|resize（a，new_shape） |返回具有指定形状的新数组。 |
|trim_zeros（filt [，trim]） |从1-D数组或序列修剪前导和/或尾随零。 |
|unique（ar [，return_index，return_inverse，...]） |查找数组的唯一元素。 |

### Rearranging elements：重新排列数组元素

| 方法                | 说明         |
| ------------------ | ------------ |
|flip  ||
|fliplr（m） |在左/右方向上翻转数组。 |
|flipud（m） |在上/下方向上翻转数组。 |
|reshape（a，newshape [，order]） |为数组提供新形状，而不更改其数据。| 
|roll（a，shift [，axis]）| 沿给定轴滚动数组元素。 |
|rot90（m [，k]） |将数组沿逆时针方向旋转90度。 |


## 索引操作：Generating index arrays

| 方法                | 说明         |
| ------------------ | ------------ |
|c_ |将切片对象转换为沿第二轴的连接。| 
|r_ |将切片对象翻译为沿第一轴的连接。| 
|s_ |为数组构建索引元组的更好方法。 |
|nonzero（a）| 返回非零元素的索引。 |
|where（条件，[x，y]） |根据条件，从x或y返回元素。 |
|indices（dimensions [，dtype]） |返回表示网格索引的数组。 |
|ix_（\ * args） |从多个序列构造一个打开的网格。 |
|ogrid |nd_grid实例，返回一个打开的多维“meshgrid”。 |
|ravel_multi_index（multi_index，dims [，mode，...]）| 将索引数组的元组转换为平面索引的数组，将边界模式应用于多索引。 |
|unravel_index（indices，dims [，order]）| 将平面索引的平面索引或数组转换为坐标数组的元组。 |
|diag_indices（n [，ndim]） |返回索引以访问数组的主对角线。 |
|diag_indices_from（arr） |返回索引以访问n维数组的主对角线。 |
|mask_indices（n，mask_func [，k]）| 给定掩蔽函数，返回索引以访问（n，n）数组。| 
|tril_indices（n [，k，m]） |返回（n，m）数组的下三角形的索引。| 
|tril_indices_from（arr [，k]） |返回arr的下三角形的索引。 |
|triu_indices（n [，k，m]） |返回（n，m）数组的上三角形的索引。| 
|triu_indices_from（arr [，k]） |返回arr的上三角形的索引。 |

### Indexing-like operations：索引操作

| 方法                | 说明         |
| ------------------ | ------------ |
|take（a，indices [，axis，out，mode]） |从轴沿一个数组中取元素。 |
|choose（a，choices [，out，mode]） |从索引数组和一组数组构造数组以供选择。 |
|compress（condition，a [，axis，out]）| 沿给定轴返回数组的所选切片。 |
|diag（v [，k]）| 提取对角线或构造对角数组。 |
|diagonal（a [，offset，axis1，axis2]）| 返回指定的对角线。 |
|select（condlist，choicelist [，default]） |返回根据条件从选择列表中的元素绘制的数组。 |

### Inserting data into arrays：插入数组数据

| 方法                | 说明         |
| ------------------ | ------------ |
|place（arr，mask，vals）| 基于条件和输入值更改数组的元素。 |
|put（a，ind，v [，mode]） |用给定值替换数组的指定元素。 |
|putmask（a，mask，values） |基于条件和输入值更改数组的元素。 |
|fill_diagonal（a，val [，wrap]） |填充给定数组的任何维数的主对角线。| 

### Iterating over arrays:遍历数组

| 方法                  | 说明         |
| ------------------  | ------------ |
|nditer               |有效的多维迭代器对象迭代数组。| 
|ndenumerate（arr）     |多维索引迭代器。| 
|ndindex              |用于索引数组的N维迭代器对象。| 
|flatiter          |平面迭代器对象在数组上进行迭代。 |
|lib.Arrayterator（var [，buf_size]） |大数组的缓冲迭代器。 |
