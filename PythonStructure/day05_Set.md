# 集合 set

1. 集合是可变的容器
2. 集合内的数据对象都是唯一的（不能重复多次)
3. 集合是无序的存储结构,集合中的数据没有先后关系
4. 集合是相当于只有键，没有值的字典，则键是集合的数据。
5. 集合内的元素必须是不可变对象
6. 集合是可迭代的(可以用for等遍历)

## 集合的生成

- 生成空的集合:   set()  
- 生成非空集合:   set(iterable) 函数  

## 集合是可迭代对象。例：

```python
s = {"abc", 123, (1970, 1, 1)}
for x in s:
   print(x)
```
用于集合的函数:len(x)/max(x)/min(x)/sum(x)/any(x)/all(x)

例：

```python
S = set([3, 5, 7, 9])
print(S)
print(max(S))
print(sum(S))

S = set("WeiMingZe")
print(S)
print(len(S))

S = set("ABCCBA")
print(S)

s = set({"name": "tarena", "age": 15})
print(s)

s = set(("ABC", 123, True))
print(s)

s = {True, None, "ABC", (1, 2, 3), 3.14}
print(s)

#输出结果如下：
{9, 3, 5, 7}
9
24
{'Z', 'e', 'M', 'i', 'g', 'W', 'n'}
7
{'B', 'A', 'C'}
{'name', 'age'}
{True, 123, 'ABC'}
{True, 3.14, 'ABC', (1, 2, 3), None}
```

## 集合的运算：

  交集，并集，补集，子集，超集  
  A = {1,2,3} 
  B = {2,3,4}
  交集 = {2, 3}
  并集 = {1, 2, 3, 4}
  补集: A - B  = {1},   B - A = {4}

集合的运算：

### `- `生成两个集合的补集
A = {1, 2, 3}  
B = {2, 3, 4}  
A - B   # 生成 {1}  
B - A   # 生成 {4}  
A - {5,6,7}  # {1,2,3}  

### `|` 生成两个集合的并集
  A = {1, 2, 3}  
  B = {2, 3, 4}  
  A | B    # {1,2,3,4}  

### `&` 生成两个集合的交集
  A = {1, 2, 3}  
  B = {2, 3, 4}  
  A & B    # {2,3}  
  {1,2} & {5, 6}   #  set()    

### `^`  生成两个集的对称补集
  A = {1, 2, 3}  
  B = {2, 3, 4}  
  A ^ B  # {1, 4}  
  A ^ B -->  (A-B) | (B-A)  

### `>` 判断一个集合是另一个集合的超集  

### `<`  判断一个集合是另一个集合的真子集
  A = {1,2,3}  
  C = {2,3}  
  A > C   # True  
  C < A   # True  

### `== / !=` 判断集合相同/不同
  A = {1,2,3}  
  C = {2,3}  
  D = {2,1,3}  
  A == D   # True  
  A == C   # False  

### `>=  <= `判断超集和相同/子集和相同
  例：略

### `in / not in `运算符
  等同于字典中的in/not in, 判断某个值是否存在于集合中,  not in 与 in 返回值相反

## Python3集合中常用的方法

S代表集合对象

| 方法                        | 说明                                  |
| ------------------------- | ----------------------------------- |
| S.add(e)                  | 在集合添加一个新元素，如果元素已经存在，则不添加            |
| S.clear()                 | 清空集合内所有的元素                          |
| S.copy()                  | 复制集合（浅拷贝)                           |
| S.difference(s2)          | 等同于 S-S2                            |
| S.difference_update(s2)   | 等同于 S=S-s2                          |
| S.discard(digit)          | 从集合S中移除一个数字，如果digit不是数字，则什么都不做      |
| S.intersection(s2)        | 等同于S & s2                           |
| S.intersection_update(s2) | 等同于S = S & s2                       |
| S.issubset(s2)            | 如果S为s2的子集返回True,否则返回False，等同于 S<=s2 |
| S.pop()                   | 从集合S中删除一个随机元素                       |
| S.remove(e)               | 从集合中删除一个元素，如果元素不存在则会产生一个KeyError错误  |
| S.union(s2)               | 生成S与s2的全集等同于` S | s2`               |
| S.update(s2)              | 等同于 S = `S | s2`                    |

## 集合推导式

语法：集合推导式可以嵌套

```python
{表达式 for 变量 in 可迭代对象 (if 条件表达式)}
```

示例：用列表转换为集合

```python
names = ["Tom", "Jerry", "Spike", "Tom", "Jerry", "Tyke"]
animals_set = {n for n in names}
```

## 固定集合 frozenset

- 创建一个不可变的，无序的，含有唯一元素的集合
- 创建空的固定集合——frozenset()
- 创建非空的固定集合——frozenset(iterable)

例：

```python
f = frozenset([1,3,5,7,9])
```

- 运算:
  &  交集、|并集、补集、^  对称补集     
  in / not in 运算、>>= < <= == != /  
  (以上运算 等同于set中的用法)

- 固定集合的方法：

相当于集合的全部方法去掉修改集合的方法。固定集合可以作为字典的键,还可以作为集合的值

-----------------
# 总结：

### 数据类型：
  bool int float complex str list tuple dict set frozenset

### 值:
  None, False, True ...

### 运算符:
`/ // % ** 、>> = < <= == != 、  
is / is not、  in / not in、  not and or、  
+= -= .、  ~ & | ^ << >>、  +(正号) -(负号)、  = 赋值(绑定)`

### 表达式：
  1+2
  input("aaaa")

### 语句:
- 赋值语句
- if 语句
- while 语句
- for 语句
- break 语句
- continue 语句
- pass 语句
- del 语句