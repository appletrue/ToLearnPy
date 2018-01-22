
# ndarray的矢量化计算：broadcastingRules

Numpy的Universal functions 中要求输入的数组shape是一致的，当数组的shape不相等时，则会使用广播机制，调整数组使得shape一样，满足规则，则可以运算，否则就出错。

矢量运算：相同大小的数组键间的运算应用在元素上 
矢量和标量运算：“广播”— 将标量“广播”到各个元素


```python
x = np.array([1,2,3]) 
x*2         # array([2 4 6])
x>2         #array([False False  True])

y = np.array([3,4,5])
x+y         #array([4 6 8])
x>y         #array([False False False])

z = np.array([2])
x*z         #array([2, 4, 6])

w = np.array([2,3])
x*w         #
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (3,) (2,)
```

## Broadcasting规则有：
Broadcasting允许通用函数以有意义的方式处理具有不完全相同形状的输入。
- 第一个规则是：让所有输入数组都向其中shape最长的数组看齐，shape中不足的部分都通过在前面加1补齐,即如果所有输入数组不具有相同数量的维度，则“1”将被重复地添加到较小数组的形状，直到所有数组具有相同数量的维度。
- 第二个规：则确保沿着特定维度具有大小为1的数组表现得好像它们具有沿着该维度具有最大形状的数组的大小。假定数组元素的值沿“Broadcasting”数组的该维度相同。
- 应用广播规则后，所有数组的大小必须匹配。



## broadcasting详细

术语broadcasting描述numpy在算术运算期间如何处理具有不同形状的数组。受限于某些约束，较小的数组依据较大数组“broadcasting”，使得它们具有兼容的形状。Broadcasting提供了一种矢量化数组操作的方法，使得循环发生在C而不是Python。它做到这一点且不用不必要的数据拷贝，通常导致高效的算法实现。然而，有些情况下，broadcasting是一个坏主意，因为它导致低效的内存使用并减慢计算。

- 输出数组的shape是输入数组shape的各个轴上的最大值
- 如果输入数组的某个轴和输出数组的对应轴的长度相同或者其长度为1时，这个数组能够用来计算，否则出错
- 当输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值

NumPy操作通常在逐个元素的基础上对数组对进行。在最简单的情况下，两个数组必须具有完全相同的形状，如下例所示：

```python
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
a * b       #array([ 2.,  4.,  6.])
```

当数组的形状满足一定的条件时，NumPy的broadcasting规则可以放宽这个限制。最简单的broadcasting示例发生在一个操作包含数组和标量值的时候：

```python
a = np.array([1.0, 2.0, 3.0])
b = 2.0
a * b       #array([ 2.,  4.,  6.])
```

结果等同于之前的示例，其中b是数组。在算术运算期间，我们可以认为标量b被拉伸了，形成与a相同形状的数组。b中的新元素是原始标量简单的拷贝。拉伸这个比喻只是概念性的。NumPy足够聪明，它使用原始的标量值而不会真正拷贝，使broadcasting操作尽可能的内存和计算高效。

第二个例子中的代码比第一个例子中的代码更有效，因为broadcasting在乘法期间移动较少的内存（b是标量而不是数组）。

```python
a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])
print(a[:, np.newaxis] + b)
#输出结果：
array([[  1.,   2.,   3.],
       [ 11.,  12.,  13.],
       [ 21.,  22.,  23.],
       [ 31.,  32.,  33.]])
```
示意图：
![Example of BroadcastingRules](https://github.com/appletrue/AboutPython/blob/master/PackagesLearn/PICs/image0020619.gif)
其本身的形状是不能改变的，只能在原来的基础上延伸，像上述的例子中，如果b的shape是(6,)，如果在broadcasting的时候reshape(6,1)则已经是属于改变了原来的数组的形状，进行了翻转，而不是延伸

## Broadcasting的一般规则

当在两个数组上操作时，NumPy在元素级别比较它们的形状。它从尾部维度开始，并向前发展。两个维度兼容，当
1.它们是相等的，或
2.其中一个是1

如果不满足这些条件，则抛出ValueError: frames are not aligned异常，指示数组具有不兼容的形状。结果数组的大小是输入数组的每个维度的最大大小。

数组不需要具有相同维度的数目。例如，如果你有一个256x256x3数值的RGB值，并且你想要通过一个不同的值缩放图像中的每个颜色，你可以将图像乘以一个具有3个值的一维数组。根据broadcast规则排列这些数组的最后一个轴的大小，表明它们是兼容的：

```
Image  (3d array): 256 x 256 x 3
Scale  (1d array):             3
Result (3d array): 256 x 256 x 3
```

当比较的任何一个维度为1时，则使用另一个。换句话说，大小为1的维被拉伸或“复制”以匹配另一维。

在以下示例中，A和B数组都具有长度为1的轴，在broadcast操作期间将其扩展为更大的大小：

```
A      (4d array):  8 x 1 x 6 x 1
B      (3d array):      7 x 1 x 5
Result (4d array):  8 x 7 x 6 x 5
```

这里有一些例子：
```
A      (2d array):  5 x 4
B      (1d array):      1
Result (2d array):  5 x 4

A      (2d array):  5 x 4
B      (1d array):      4
Result (2d array):  5 x 4

A      (3d array):  15 x 3 x 5
B      (3d array):  15 x 1 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 1
Result (3d array):  15 x 3 x 5
```

以下是不broadcast的形状示例：
```
A      (1d array):  3
B      (1d array):  4 # trailing dimensions do not match

A      (2d array):      2 x 1
B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched
```

