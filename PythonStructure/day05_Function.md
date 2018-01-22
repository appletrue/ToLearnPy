# 函数 function

## 1、什么是函数:

函数是一段可执行的代码块，可以重复使用

## 2、函数作用：

1，划分功能模块，更好管理软件工程（协同开发）；
2，复用代码，减少开发工作量；
3，提高代码阅读性，降低维护成本；

## 3、函数定义:

```python
def 函数名(参数列表):
	"注释块"
	语句块(代码块)...如 pass
	return [返回值]（可选）
```

## 语法说明：

1. 函数代码块以 def关键词开头，后接函数标识符名称和圆括号()；
2. 函数名是语句块（代码块）的名称，其命名规则与变量名相同(标识符)；
3. 函数本身也是一个变量，该变量类型就是可调用类型,属性只读；
4. 函数有自己的命名空间，要让函数处理外部数据需要用参数给函数传入一些数据,任何传入的参数和自变量作为参数列表必须放在圆括号中间。如果不需要传入参数，参数列表可以为空；
5. 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
6. 函数内容以冒号起始，并且缩进；
7. 语句块部分不能为省略，如果为空语句，需要填充pass关键字。
8. return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

示例：
```python
def hello():
    print("hello!")

def hellon(n):
    while n:
        print("hello!")
        n -= 1

def add(a, b):
    return a + b

hello()
hellon(3)
print(add(2,3))

#输出结果如下：
hello!
hello!
hello!
hello!
5
```

## 4、函数调用:

函数名(实际参数)

调用说明:

1. 函数调用是一个表达式
2. 如果没有return语句，函数执行完毕返回None 值对象
3. 如果函数需要返回其它的值对象需要用return语句
4. 函数调用作为模块内部语句时，必须先定义函数，后调用函数

示例：
```python
hello()
hellon(10)
a = add(10,20)
print(a)
```
## 5、函数返回：

return 语句

- 语法:
  return [表达式]  
  []代表可选

- 作用：
  结束当前函数的执行，返回到调用该函数的地方，同时返回一个值对象的引用关系

- 说明：

1. return 语句后跟的表达式可以省略，省略后相当于return None  
2. 如果函数内没有return 语句，则函数执行完最后一条语句后返回None（相当于在最后加了一条 return None语句）  
3. 函数的调用可以返回一个值或一组值

注：python函数定义的结束，是以遇到与def同级语句为标志；

示例：

```
def sub(a,b):
	return a-b

def max_min(a,b,c):  	# 比较3⃣️三个数字的大小
   if a>= b:
        max = a
        min = b
    else:
        max = b
        min = a
    if c > max:
        max = c
    elif c < min:
        min = c
    return (max,min)

x = sub(23,31)
print(x)
y = max_min(11,12,13)
print(y)

# 
-8
(13, 11)
```

## 6、函数的参数传递：

传递方式：

1. 位置传参
2. 关键字传参
3. `*` 序列传参
4. `**` 字典关键字传参
5. 综合传参

### 位置传参:

实际参数的对应关系与形式参数的对应关系是以位置来依次对应的

示例：

```python
def sum3(a,b,c):
    pass
print("a=",a)
print("b=",b)
print "c=",c)
x = sum3(1,2,3)
x = sum3(1,2) #error	
```

位置传参说明：
- 实参和形参通过位置进行对应和传递  
- 实参和形参的个数必须完全相同

### 关键字传参：

关键字传参是指传参时，按着形参的名称给形参赋值，实参和形参按名称进行匹配．
示例：

```python
sum3(a=1,b=2,c=3)
sum3(b=2,a=1,c=3)
sum3(b=2,a=1)	#缺少关键字参数
sum3(b=2,a=1,c=3,d=9)	#错误，没有d这个参数
sum3(b=2,a=1,3)	#缺少关键字
```

###  `*`序列传参：

序列类型（list，tuple，str）作为参数列表传递，其要求是：序列的元素个数必须与参数的个数相同

示例：

```python
def myfun(a, b, c):
    print("a-->", a)
    print("b-->", b)
    print("c-->", c)
    
# 序列传参
s1 = [11, 22, 33]  # 列表
myfun(*s1)  # 等同于　myfun(s1[0], s1[1], s1[2])
s2 = (1.1, 2.2, 3.3)  # 元组
myfun(*s2)
s3 = "ABC"  # 字符串
myfun(*s3)
#输出结果：
a--> 11
b--> 22
c--> 33
a--> 1.1
b--> 2.2
c--> 3.3
a--> A
b--> B
c--> C
```
### 不定长参数:`*`星号元组形参

语法:
```
def 函数名(*元组形参名):
    语句块
```

示例: 
```
def myfun(*args):
	print("实参个数是", len(args))
	print(args)
	i = 1
	for x in args:
	    print("第", i, "个参数是:", x)
	    i += 1
myfun(1, 2)
print('----------------------')
myfun("100", 200, "Three", 4.4)

#输出结果
实参个数是 2
(1, 2)
第 1 个参数是: 1
第 2 个参数是: 2
----------------------
实参个数是 4
('100', 200, 'Three', 4.4)
第 1 个参数是: 100
第 2 个参数是: 200
第 3 个参数是: Three
第 4 个参数是: 4.4
```

### `**`字典关键字传参:

- 不定长参数:`**`双星号字典形参

实参和形参通过字典进行传递和匹配,字典的值传递给键对应的形参

说明:
- 字典传参的键名和形参名必须一致  
- 键名必须为字符串  
- 键名要在形参中存在

示例: 

```
d1 = {"c":33, "a":11, "b":22}
myfun(**d1)	#ok
d2 = {"c": 33, "a": 11, "b": 22,"d":100}
myfun(**d2)	#error，d不存在
d3 = {"c": 33, "a": 11}
myfun(**d3)	#error,少一个argument
```

语法:
```
def 函数名(**字典形参名):
	语句
```
示例:
```
def myfun(**kwargs):
  print("参数个数:", len(kwargs))
  for k,v in kwargs.items():
      print(k, "->>", v)
#调用
  myfunc(name="Midu", age=15)			#ok
  myfunc(a=1, b="BBB", c=[1,2,3], d=True)	#ok
  myfun(1,2,3)  # 错的
  myfun(name="midu",35)
```

### 综合传参 

以上几种方式的混合使用

myfun(100, *(200, 300))

## 7、函数的缺省参数

函数的形参如果被赋予默认参数值，那么该函数在调用时，如果对应的形参没有实参进行值传递，则使用默认值计算；

语法:

```python
def 函数名(形参1=默认参数值1, 形参2=默认参数值2,...):
	语句
```

示例: 
```
def info(name, age=1, sex="none"):
    print("name", name, "age:", age, "sex:", sex)
```

调用时

```python
info("sam", 35, "male")
info("rose", 15)
info("tina")
def get_round(r,pi=3.1415926):
  	...
    get_round(10)
  	get_round(10,pi=3.1415926567856)
```

——缺省参数说明：

1. 缺省参数必须自右至左依次存在，如果一个参数有缺省值，则其右侧的所有参数都必须有缺省参数(缺省值)  
2. 缺省参数可以有0个或多个,甚至全部是有缺省参数

例:
```python
def fn(a, b=10, c): 
    pass    	 # 这是错的
def fn(a = 1, b, c=3): 
    pass  	# 这是错的
```

### 命名关键字形参

语法:
```
def 函数名(*, 命名关键字形参名)
	语句块
```
  或
```
def 函数名(*args, 命名关键字形参名)
	语句块
```

示例:

```
def myfun1(a, b, *, c):  # c 为命名关键字形参
    print(a, b, c)
myfun1(1, 2, c=3)   # 对的
myfun1(11, 22, 33)  # 错的
myfun1(11, c=22, b=33)  # OK
def myfun2(a, *args, b, c):  # b,c为命名关键字形参
    print(a, b, c, args)
myfun2(1, 2, 3, 4)  # 错的
myfun2(1, 2,5,6,7, b=3, c=4)  # 对的
myfun2(11, c=44, b=33)   # 对的
```

## 8、函数的参数列表顺序:

位值形参,缺省参数,星号元组形参,双星号字典形参,命名关键字参数可以混合使用

函数参数自左至右的顺序为：  位置形参, 星号元组形参, 命名关键字参数,双星号字典形参，默认。
例:

```
def fn(a, b, *args, c, **kwargs):
	pass
fn(100, 200, 300, 400, c="C", d="D", e="E")
```
详细语法: 见:  help("def")

### 9、 可变／不可变类型的实参的参数传递的区别

- 可变类型：列表list, 集合set, 字典dict
- 不可变类型:  frozenset, tuple, str, numbers

问题：函数只能通过返回值传回数据吗？

示例1：

```python
L = []
def fn(x):
    x.append(10)
fn(L)
print(L)  #　[10]
fn(L)
print(L)  # [10, 10]

D = {}
def fn(x):
    x['name'] = "sam"
fn(D)
print(D)

#输出结果如下：
[10]
[10, 10]
{'name': 'sam'}
(1, 2, 3)
```
示例2:
```python

t = (1,2,3)
def fn(x):
    x[1] = 2.2
print(t)
#fn(t)  # 对元组赋值出错TypeError: 'tuple' object does not support item assignment
X =100
def fn(x):
    x=200
fn(X)
print(X)

#输出结果如下：
(1, 2, 3)
100
```

区别：
- 不可变的类型的数据作为函数参数传入时，函数内部不会改变变量的原数据值，是安全的；  
- 可变类型的数据作为参数传入时，函数内部可以改变原数据，多用来返回更多数据结果

### 10.函数的属性:

###　｀__name__｀ 属性

作用：用来记录函数名

说明：以双下划线开头，以双下划线结尾的标识符通常代表python的特殊属性等．

示例:（function_attribute/__name__.py）
```python
def abc():
	pass

a = abc
print(a.__name__)  # abc

def xxx(fn):
    if fn.__name__ == "abc":
        print("exec abc")
    elif fn.__name__ == "max":
	print("exec max")

xxx(abc)
```

###　｀__doc__｀ 属性

用于记录文档字符

示例：(function_attribute/__doc__.py)
```python
def cba():
    "我是文档字符串"
    pass

print cba.__doc__
```