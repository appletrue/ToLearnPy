
# 拷贝和视图

当计算和操作数组时，它们的数据有时被复制到新的数组中，有时不复制。这通常是初学者的混乱的来源。有三种情况：

## 完全不复制

简单赋值不会创建数组对象或其数据的拷贝。

```python
a = np.arange(12)
print(b = a)   # no new object is created
print(b is a)  # a and b are two names for the same ndarray object
               # True
print(b.shape = 3,4)    # changes the shape of a
print(a.shape)        #(3, 4)
```

Python将可变对象作为引用传递，因此函数调用不会复制。

```python
def f(x):
    print(id(x))

id(a)   # id is a unique identifier of an object
        #148293216
f(a)    #148293216
```

## 视图或浅拷贝

不同的数组对象可以共享相同的数据。view方法创建一个新数组对象，通过该对象可看到相同的数据。

```python
c = a.view()
print(c is a)       #False
print(c.base is a)  # c is a view of the data owned by a
                    # True
print(c.flags.owndata)  #False
print(c.shape = 2,6)    # a's shape doesn't change
print(a.shape)      #(3, 4)
c[0,4] = 1234    # a's data changes
print(a)

#输出结果：

array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])
```

对数组切片返回一个视图：

```python
s = a[ : , 1:3]     # spaces added for clarity; could also be written "s = a[:,1:3]"
s[:] = 10           # s[:] is a view of s. Note the difference between s=10 and s[:]=10
print(a)
#输出结果：
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```

## 深拷贝

copy方法生成数组及其数据的完整拷贝。

```python
d = a.copy()    # a new array object with new data is created
print(d is a)     #False
print(d.base is a)     # d doesn't share anything with a
                  #False
d[0,0] = 9999
print(a)
#输出结果：
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```
