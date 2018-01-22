# 字典 dict

## 什么是字典:

1. 字典是一种可变的容器，可以存储任意类型的数据
2. 字典中的每个数据都是用"键" (key) 进行索引，而不像序列可以用下标进行索引
3. 字典中的数据没有先后关系，字典的存储是无序的
4. 字典的数据是以键(key)-值(value)对的形式进行存储的
5. 字典的表示方式是以{} 括起来，以冒号(:)分割的键值对，各键值对之间用逗号分隔开
6. 字典的键不能重复

## 创建空字典的方法:字典的生成函数:

- dict()   生成一个字典，等同于{}
- dict(iterable)  用可迭代对象初始化一个字典
- dict(**kwargs)  关键字参数形式生成一个字典

例：

```python
d = dict()
d = dict([('name', 'tarena'), ('age', 15)])
d = dict(name="tarena", age=16)
name = "weimingze"
{'name' : name}
```
```python
d = {}     # 空字典
d = dict() # 空字典
```
## 创建非空的字典的方法：

```python
d = { "name": "weimingze", "age": 35}
d = { "name": None, "age": 1}
```

以下写法存在问题

```python
d = { "a": 1, "b": 2, "a": 1.1} # 去掉重复的键
```

- 字典的值(value)可以为任意类型:  字典的值可以是布尔值，数据，字符串，None,列表，元组，字典，以及后面要学到的集合，函数，类对象等所有类型。例：

```python
{"a" : 100 }
{"a" : "abc" }
{"a" : True }
{"a" : None }
{"a" : [1,2,3] }
{"a" : (1,2,3) }
{"a" : {"aa":11 } }
```

## 字典的键(key)必须为不可变类型的值

- 不可变的类型

  bool, int, float, complex, str, tuple, frozenset(固定集合),  包括：None

- 不能充当键的类型有:

  列表list,字典dict,集合set.例：

```python
{"a": "a"}
{100: "100"}
{True: "True"}
{None: "abc"}
{(1970, 1, 1): "computer year!"}
```

## 字典的基本操作：

### 字典的访问：

用[]运算符访问字典内的成员:　字典[键].
例：

```python
d = {"name": "tarena", "age": 15}
print("姓名：", d["name"], "年龄：", d["age"])
```

### 字典的遍历：

```python
d={1:100, 2:200， 3:300}
for k,v in d.items():
	print k,":", v
```

### 添加／修改字典的元素

字典[键] = 值——[key]:Value
- 增加：键不存在，创建键，并绑定键对应的值
- 修改：键存在，修改键绑定的值
  例：

```python
d = {}
d['name'] = 'tarena'  # 创建新的键值对
d['age'] = 15         # 创建新的键值对
d['age'] = 16         # 修改age键所对应的值
```

### 删除字典元素 del

del 字典[键].例：
del d['age']  # 删除年龄和其对应的值

### 字典的成员资格判断—— in / not in 运算符

可以用in /not in 运算符来判断一个键是否存在于字典中,如果存在则返回True,否则返回False。   
not in 与 in相反

例：

```python
d = {'age': 16, 'name': 'tarena'}
"age" in d   # True
16 in d      # False
```

## 字典的基本函数操作：

- len(x) 返回字典的长度
- max(x) 返回字典的键的最大值
- min(x) 返回字典的键的最小值
- sum(x) 返回字典中所有键的和
- any(x) 真值测试,任意键为真，则返回True,否则为False
- all(x) 真值测试，所有键为真值，则返回True,否则为False

示例：获取字典中元素个数len函数:
- len(字典)　返回字典的元素(键值对)个数

```python
d = {3 : "333", 8 : "888", 5 : "555"}
len(d)  # 3
max(d)  # 8
min(d)  # 3
sum(d)  # 16
```

## 字典的方法:

D代表字典对象

| 方法                  | 说明                              |
| ------------------- | ------------------------------- |
| D.clear()           | 清空字典                            |
| D.pop(key)          | 移除键，同时返回此键所对应的值                 |
| D.copy()            | 返回字典D的副本，只复制一层（浅拷贝)             |
| D.update(D2)        | 将字典D2合并到D中，如果键相同，则此键的值取D2的值作为新值 |
| D.get(key, default) | 返回键key所对应的值，如果没有此键则返回default    |
| D.keys()            | 返回可迭代的dict_keys集合对象             |
| D.values()          | 返回可迭代的dict_values值对象            |
| D.items()           | 返回可迭代的dict_items对象              |

```python
D = {1: "1", 2: "2"}
D2 = {2: "2.2", 3: "3.3"}
D3 = D.update(D2)
print(D)    # D = {1 : "1", 2: "2.2", 3: "3.3"}
# print(D3)   # None
for k in D.keys():
    print(k)  # 1 2 3
for v in D.values():  # 打印所有的值
    print(v)
for i in D.items():
    print(i)
#输出结果如下：
{1: '1', 2: '2.2', 3: '3.3'}
1
2
3
1
2.2
3.3
(1, '1')
(2, '2.2')
(3, '3.3')
```

```python
for k, v in D.items():
    print("键", k, "--->", v)
```

## 字典推导式:

语法：{ 键表达式 : 值表达式 for 变量 in 可迭代对象  (if 条件表达式) }

示例：

```python
numbers = [1001, 1002, 1003, 1004]
names   = ["Tom", "Jerry", "Spike", "Tyke"]
animals = { numbers[i] : names[i] for i in range(4)}
print(animals)
animals = { numbers[i] : names[i] for i in range(4) if numbers[i] % 2 == 0}
print(animals)
#输出结果如下：
{1001: 'Tom', 1002: 'Jerry', 1003: 'Spike', 1004: 'Tyke'}
{1002: 'Jerry', 1004: 'Tyke'}
```

字典也是可迭代的对象。例：

```python
d = {"name": "tarena", (2002, 1, 1): "生日"}
for x in d:
    print(x)
#输出结果如下：
name
(2002, 1, 1)
```
 **总结** ：三种可变的数据类型：list、dict、set