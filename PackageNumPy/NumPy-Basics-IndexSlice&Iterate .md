# 索引、切片和迭代

一维数组可以索引，切片和迭代，非常类似于列表和其他Python序列。

```python
a = np.arange(10)**3
print(a)            #array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
print(a[2])         #8
print(a[2:5])       #array([ 8, 27, 64])
a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
print(a)            #array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
print(a[ : :-1])                                 # reversed a
                    #array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])
for i in a:
    print(i**(1/3.))
#
nan
1.0
nan
3.0
nan
5.0
6.0
7.0
8.0
9.0
```

多维数组每个轴可以有一个索引。这些索引以逗号分隔的元组给出：

```python
def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)
#
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
print(b[2,3]) 	#==>b[2][3],23
print(b[1])       #array([10, 11, 12, 13])
print(b[0:5][1])    #array([10, 11, 12, 13])
print(b[1][:])      #array([10, 11, 12, 13])
print(b[:][1])      #array([10, 11, 12, 13])
print(b[0:5, 1])   # each row in the second column of b
                    #array([ 1, 11, 21, 31, 41])
print(b[ : ,1])   # equivalent to the previous example
                  #array([ 1, 11, 21, 31, 41])
print(b[1:3, : ])  # each column in the second and third row of b
#输出如下：
  array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
```

当提供比轴数更少的索引时，缺失的索引被认为是一个完整切片:

```python
b[-1]   # the last row. Equivalent to b[-1,:]
#输出结果：
array([40, 41, 42, 43])
```

b[i]方括号中的表达式i被视为后面紧跟着:的多个实例，用于表示剩余轴。NumPy也允许你使用三个点写为b[i,...]。

**三个点（...）**表示产生完整索引元组所需的冒号。

例如，如果x是rank为的5数组（即，它具有5个轴），则

x[1,2,...]等效于x[1,2,:,:,:]

x[...,3]等效于x[:,:,:,:,3]

x[4,...,5,:]等效于x[4,:,:,5,:]

```python
#a 3D array (two stacked 2D arrays)

c = np.array( [[[  0,  1,  2],   
                [ 10, 12, 13]],
               [[100,101,102],
                [110,112,113]]])
print(c.shape)          #(2, 2, 3)
print(c[1,...])      # same as c[1,:,:] or c[1]
#输出结果：

array([[100, 101, 102],
       [110, 112, 113]])
       
print（c[...,2]）      # same as c[:,:,2]

#输出结果：
array([[  2,  13],
       [102, 113]])
```

对多维数组的迭代是相对于第一个轴完成的：

```python
for row in b:
    print(row)
# 输出结果
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```

但是，如果想对数组中的每个元素执行一个操作，可以使用flat属性，它是一个迭代器

```python
for element in b.flat:
     print(element)
#输出结果：
0
1
2
3
10
11
12
13
20
21
22
23
30
31
32
33
40
41
42
43
```
