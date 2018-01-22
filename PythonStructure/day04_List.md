# 列表

- 定义:
  列表是由一系列特定元素组成的．元素之间可能没有任何关联，但他们之间有先后顺序关系．

- 列表可以改变各个元素的值；列表是一种容器

## 空列表：

```python
L = []      # 空列表
L = list()  # 空列表
#创建非空列表：
L = [1, 2, 3, 4]
L = ["Beijing", "Shanghai", "Shenzhen"]
L = [1, "two", 3.0, 'four']
L = [1, 2, [3.1, 3.2], 4]  
```

### 列表的生成函数 list()

—— list()  生成一个空列表，等同于[]  
—— list(iterable)   用可迭代对象初始化一个列表 
例：

```python
L = list("hello")  # L--> ['h', 'e', 'l', 'l', 'o']
S = 'tarena'       # tarena
#L = list(S)       # ['t', 'a', 'r', 'e', 'n', 'a']
print(L)           # ['t', 'a', 'r', 'e', 'n', 'a']
print(S) 
```

# 列表的运算

————算术运算：`+  +=  *  *=`

### `+`加号运算符用于拼接列表
例:

```python
x = [1,2,3]
y = [4,5,6]
print(x + y)    # [1, 2, 3, 4, 5, 6]
```

### `+=` 运算符用于原列表与右侧列表拼接生成新的列表

```python
x = [1,2,3]
y = [4,5,6]
x += y    # 等同于 x = x + y
x += y
print(x)  # [1, 2, 3, 4, 5, 6]
```

### `-`运算符用于生成重复的列表

```python
x = [1, 2] * 3 
print（x)  # x = [1,2,1,2,1,2]
```

### `*=` 用原列表生成重复的列表，并改变变量的绑定

```python
x = [1,2,3]
x *= 4  
print(x)    # x = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### 列表的关系(比较)运算:`>> = < <= == !=`
例：

```python
x = [1,2,3]
y = [2,3,4]
print(x != y)  # True
print(x == y)  # False
print(x > y)   # False
print(x < y)  # True
print([1,"two"] < ["two",1])  #TypeError: '<' not supported between instances of 'int' and 'str'
```

### 列表的in / not in 运算符

```python
x = [1, 'two', 3.0, "four"]
print(1 in x)  # True
print(2 not in x)  # True
print("3" in x)  # False
print(10 in x) # False
```

# 列表的基本操作：

### 索引 index —— 列表[索引]
列表是可变的，可以通过索引赋值改变列表的元素

等同于字符串索引:
- 正向索引: 0 ~ len(x)-1  
  — 反向索引: -len(x) ~ -1    

例：

```python
x = [1,2,3,4]
x[2] = 3.14
print(x)  # [1, 2, 3.14, 4]
```

### 切片 slice

列表切片的规则等同于字符串切片规则：[:] [::]

例:

```python
x = [1,2,3,4,5]
y = x[1::2]  # y = [2, 4]
```

### 切片赋值:

- 切片赋值可以改变原列表的排列，及插入、删除数据.  列表中可以用切片改变列表对应元素的值

例：
```python
L = [2, 3, 4]
L[0:1] = [1.1, 2.2]
print(L)                 # L= [1.1, 2.2, 3, 4]
L[2:] = [3.3, 4.4, 5.5]  # L=[1.1,2.2,3.3,4.4,5.5]
print(L)
L[:] = [3, 4]  # L = [3,4]
print(L)
L = [1, 2, 3, 4, 5, 6]
L[0::2] = [1.1, 3.3, 5.5]  # 步长为 2 替换原列表中的元素
print(L)
L[0::2] = [0.1, 0.2]  # ValueError: attempt to assign sequence of size 2 to extended slice of size 3

```
- 对于步长为1的切片赋值：完成的功能是连续替换，等号左右总数可以不等。
  例：
```python
L = [2, 3, 4]
L[0:1] = [1.1, 2.2]  
print(L)                 # L= [1.1, 2.2, 3, 4]
L[2:] = [3.3, 4.4, 5.5]  
print(L)                 # L=[1.1,2.2,3.3,4.4,5.5]
L[:] = [3, 4]  
print(L)                 # L = [3,4]
L[:] = [1, 2, 3, 4, 5, 6]
print(L)                 #[1, 2, 3, 4, 5, 6] 
```

注意事项：
对于步长大于1的切片赋值，完成的功能是逐一替换，因此等号左右数要一致，否则会出现赋值错误！
例：

```python
L = [1,2,3,4,5,6]
L[::2] = "ABC"   # 对的
print(L)                 # L= [1.1, 2.2, 3, 4]
L[::2] = "ABCD"  # 错的
print(L)                 # ValueError: attempt to assign sequence of size 4 to extended slice of size 3
```

- 切片赋值是改变原列表，不会生成新列表

```python
L = [1,2,3,4,5,6]
L2 = L
L3 = L[::2]  # [1,3,5]
print(L2)
print(L3)
L[::2] = [.1, .3, .5]
print(L)       # [0.1, 2, 0.3, 4, 0.5, 6]
```
- 切片被字符串赋值时，字符串是按字符去替换。
```python
L = [1,2,3,4,5,6]
L[::2] = "ABC"   # L=['A',2,'B',4,'C',6]
L[::2] = "ABCD"  # 错的
```

### python3中常用的序列函数  

- len(x)  返回序列的长度
- max(x)  返回序列的最大值的元素 
- min(x)  返回序列的最小值的元素
- sum(x)  返回序列中所有元素的和
- any(x)  真值测试，如果列表其中一个值为真值，则返回True
- all(x)  真值测试，如果列表中所有值都为真值则返回True

例:

```python
L = [1, "two", 3.0]
print(len(L))    # 3
L = [8, 3, 6, 2]
print(max(L))   # 8
print(min(L))   # 2
```

### python3中列表的常用方法——见: >>> help(list)

以下L代表列表

L.index(v[,begin[,end]])  返回对应元素的索引下标,begin为开始索引，end为结束索引
L.insert(index, obj)  		将某个元素插放到列表中指定的位置
L.count(x)  				      返回列表中元素的个数
L.remove(x)  				      从列表中删除第一次出现在列表中的值
L.copy()    				      复制此列表(只复制一层,不进行深层复制)
L.append(x) 				      在列表尾部添加单个元素
L.extend(lst) 				    向列表追加另一个列表
L.clear()   				      清空列表，等同于L[:] = []
L.sort(reverse=False) 	 	将列表的顺序按值的小到大顺序进行排列(升序),reverse=True(降序)
L.reverse()   				    列表反转
L.pop([index]) 			      删除索引对应的元素，如果不加索引，默认删除最后元素，同时返回移除元素

### 列表嵌套：

```python
L = [20, 21, 22]
L1 = [10, L, 30]
L2 = L1.copy()
L[2] = 25
print(L1)   # [10, [20, 21, 25], 30]
print(L2)   # [10, [20, 21, 25], 30]
```

### 复制列表：  深拷贝和浅拷贝

- 浅拷贝 shallow copy

```python
L = [20, 21, 22]
L.copy() 
L[:]    # 切片复制是浅拷贝
```

- 深拷贝 deep copy：将对象逐层复制（复制后的对象完全独立)

```python
import copy  # 导入copy模块
L = [20, 21, 22]
L1 = [10, L, 30]
L2 = copy.deepcopy(L1)  # 调用深拷贝函数进行复制
L[2] = 25
print(L1)   # [10, [20, 21, 25], 30]
print(L2)   # [10, [20, 21, 22], 30]
```

### del 运算符用于删除列表元素

例：

```python
cities = ["北京", "上海", "深圳", "天津"]
cities.remove("深圳")  # 删除“深圳” ['北京', '上海', '天津']
print(cities)
cities.pop(2)
print(cities)         # ['北京', '上海']
del cities[2]         # 删除列表中的元素
print(cities)
```

### 列表是可迭代对象

```python
L = [2, 3, 5, 7]
for x in L:
    print(x)
```

### 列表推导式 (list comprehension)

列表推导式是用可迭代对象，依次生成列表内元素的方式

语法：

```python
  [表达式 for 变量 in 可迭代对象]
  或
  [表达式 for 变量 in 可迭代对象 if 条件表达式]
```
例如： 要生成如下列表
L = [1, 4, 9, 16, 25, 36, 49, 64, 81, 121]
[1**2, 2**2, 3**2, 4**2, ....]
 [1, 9, 25, 49, 81]
```python
L = [x**2 for x in range(1, 11)]
print(L)                        # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
L = [x**2 for x in range(1, 11) if x % 2 == 1]
print(L)                        # [1, 9, 25, 49, 81]
```

### 列表推导式的嵌套：

语法:

**[ 表达式1 for 变量1 in 可迭代对象1 (if 条件表达式1) for 变量2 in 可迭代对象2 (if 条件表达式2)]**

示例：将列表[2,3,5] 中的元素与 列表 [7, 11, 13]的元素分别相乘，将得到的元素放于一个列表中

```python
 L = [x*y for x in [2,3,5] for y in [7,11,13]]
```

## 列表和字符串比较

1.都是序列，有先后顺序

2.列表是可变的，字符串是不可变的

3.列表可以存储任意类型的数，字符串只能存储字符

## 字符串的文本解析方法:

S.split(sep=None)  将字符串S分割为字符串列表    
S.join(iterable)   将可迭代对象进行拼接，中间用字符串进行分隔

例：
```python
s = 'welcome to tarena'
words = s.split(' ')  # ['welcome', 'to', 'tarena']
```