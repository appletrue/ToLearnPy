编程思想

================================================

# 函数式编程定义

函数式编程是指使用一系列的函数解决问题。函数仅接受输入并产生输出，不包含任何能影响产生输出的内部状态。任何情况下，使用相同的参数调用函数始终能产生同样的结果。

在一个函数式的程序中，输入的数据“流过”一系列的函数，每一个函数根据它的输入产生输出。函数式风格避免编写有“边界效应”(side effects)的函数：修改内部状态，或者是其他无法反应在输出上的变化。完全没有边界效应的函数被称为“纯函数式的”(purely functional)。避免边界效应意味着不使用在程序运行时可变的数据结构，输出只依赖于输入。 

可以认为函数式编程刚好站在了面向对象编程的对立面。对象通常包含内部状态（字段），和许多能修改这些状态的函数，程序则由不断修改状态构成；函数式编程则极力避免状态改动，并通过在函数间传递数据流进行工作。但这并不是说无法同时使用函数式编程和面向对象编程，事实上，复杂的系统一般会采用面向对象技术建模，但混合使用函数式风格还能让你额外享受函数式风格的优点。

当编译器遇到 def，会 成创建函数对象指令。也就是说 def 是执 指令， 不仅仅是个语法关键字。可以在任何地方动态创建函数对象。 

一个完整的函数对象由函数和代码两部分组成。其中，PyCodeObject 包含了字节码等执 数据，而PyFunctionObject 则为其提供了状态信息。

函数声明:
```python
def name([arg,... arg = value,... *arg, **kwarg]):
    suite
```
结构定义:
```python
typedef struct {
    PyObject_HEAD 		 
    PyObject *func_code;		#PyCodeObject
    PyObject *func_globals;		#所在模块的全局名字空间  
    PyObject *func_defaults;		#参数默认值列表
    PyObject *func_closure;		#闭包列表
    PyObject *func_doc;			#__doc__
    PyObject *func_name; 		#__name__
    PyObject *func_dict; 		#__dict__
    PyObject *func_weakreflist;		#弱引 链表
    PyObject *func_module;		#所在 Module
} PyFunctionObject;
```

### 有边界效应的函数：（不可重入的函数）

使用了全局变量，静态变量，或者处理的数据不全是来自函数的输入（比如来自硬件）的。
例如：
```python
y = 200
def myadd(x):
    return x + y

print(myadd(10)) # 210
y = 300
print(myadd(10)) # 310
```
### 纯函数式：（可重入的函数）

类似数学函数的映射，给定输入，就会得到指定输出，没有任何副作用的。
例如：
```python
def add2(x, y):
    return x + y
```

## 函数式编程的好处:

- **逻辑可证**
  这是一个学术上的优点：没有边界效应使得更容易从逻辑上证明程序是正确的（而不是通过测试）。 
- **模块化**
  函数式编程推崇简单原则，一个函数只做一件事情，将大的功能拆分成尽可能小的模块。小的函数更易于阅读和检查错误。 
- **组件化** 
  小的函数更容易加以组合形成新的功能。 
- **易于调试**
  细化的、定义清晰的函数使得调试更加简单。当程序不正常运行时，每一个函数都是检查数据是否正确的接口，能更快速地排除没有问题的代码，定位到出现问题的地方。 
- **易于测试**
  不依赖于系统状态的函数无须在测试前构造测试桩，使得编写单元测试更加容易。 
- **更高的生产率**
  函数式编程产生的代码比其他技术更少（往往是其他技术的一半左右），并且更容易阅读和维护。

## 函数式编程的基础风格特征：

- 函数是一等公民

函数能作为参数传递，或者是作为返回值返回。

- 函数变量

函数名是变量，它在创建函数时绑定一个函数对象
例：
```python
def fn():
 	print("hello world")
f1 = fn
f1()  #　等同于调用函数fn() 
	  # hello world
```

## 高阶函数(Higer-Order-Function):

### 什么是高阶函数:

满足下列条件中的一个的函数即为高阶函数:
1. 函数接受一个或多个函数作为参数传入
2. 函数返回一个函数

#### 函数作为函数的返回值

示例：（functional_programming/return_fn.py）
```python
def getfn():
    def print_hello():
        print("hello")
    return print_hello

fn = getfn()
fn()		#hello
```
#### 函数作为函数的参数传递:

示例：

```python
def tab(x, y):
    return "|" + x.center(13) + \
    "|" + y.center(13) + "|"

def string(x, y):
    return "姓名:" + x  + ",年龄:" + y

def myprint(fx, x, y):
    s = fx(x, y)
    print(s)

myprint(string, "sam", "21")
myprint(string, "rose", "23")
myprint(tab, "sam", "21")
myprint(tab, "rose", "23")

# 输出结果如下：
姓名:sam,年龄:21
姓名:rose,年龄:23
|     sam     |      21     |
|     rose    |      23     |
```
示例2:

```python
def goodbye(L):
    for x in L:
    print("bye,", x)

def hello(L):
    for x in L:
    print("hello,", x)

def operator(fn, L):
  	fn(L)

operator(hello, ["sam", "rose"])
operator(goodbye, ["sam", "rose"])

# 输出结果如下：
hello, sam
hello, rose
bye, sam
bye, rose
```

## 偏函数

函数有很多参数时，如果固定住一些参数，可以利用functools模块Partial得到一个偏函数，方便以后的使用。

示例：
```python
print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))

#输出结果如下：
12345
5349
74565
```
###偏函数设定

```python
import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
```

迭代器（暂略，置后讲）

可以用for进行循环变量的可迭代对象。
​	
--------------------------------------------------------------
生成器（暂略，置后讲）
	生成器（generator）是一种创建迭代器的方法。
--------------------------------------------------------------

# 封装控制结构的内置模板函数 

Python中内置(builtins)的高阶函数
- map, 
- reduce, 
- filter, 
- sorted

## map函数:

map(func, *iterable) 用函数func和可迭代对象iterable中的每个元素作为参数计算出新的可迭代对象,当最短的一个可迭代对象完成迭代后,此迭代生成结束.

例: 生成一个迭代器,此迭代器可以生成1~9的自然数的平方
```python
def power2(x):
    return x ** 2
#print(power2(6)) #test

mit = map(power2, range(1, 10))
for x in mit:
    print(x, end=' ')
#输出结果如下：
36
1 4 9 16 25 36 49 64 81
```

例：生成一个迭代器,此迭代器可以生成 1*4, 2*3, 3*2, 4*1这样的数

```PYTHON
def mymul(x, y): 
    return x*y
mit = map(mymul, [1,2,3,4], [4,3,2,1])
[x for x in mit]  # [4, 6, 6, 4]

pow(x, y, z = None)  
```
练习： 给出一个数n,写一个函数计算1+2**2+3**3+...+n**n的和
  注意:n给个小点的数

用pow, sum, map, range 函数组成出结果?
上题用函数式编程来做


练习:求:1**9+2**8+3**7+.....9**1的和 11377
用函数式编程来求:
pow, sum, map, range
lambda

## reduce 函数

reduce(function, iterable[, initializer])

- 作用：

reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

- 说明：

参数解释：
function -- 函数，有两个参数
iterable -- 可迭代对象
initializer -- 可选，初始参数
​	
示例：
```python
def add(x, y) :            # 两数相加
...     return x + y
... 

·>>>reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
	#	[3,6,10,15]
15
```

## filter 函数

- 语法：  filter(function or None, iterable)

- 作用:筛选iterable中的数据,返回一个可迭代对象,此可迭代对象将对iterable进行筛选.

- 说明:
  function将对iterable中的每个元素进行求值,返回False则将此数据丢弃,返回True,则保留此数据

示例1：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def is_odd(n):
    return n % 2 == 1
 
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist) 
```
示例2：
```python
  L = [x for x in range(10)]  # [0,1,2,3,...9]

  def isodd(x):   # 如果为奇数返回True
      return x % 2 == 1
  L2 = [x for x in filter(isodd, range(10))]
  print L2
```

## sorted 函数

- 作用:将原可迭代对象的数据进行排序,生成排序后的列表
- 格式:sorted(iterable, key=None, reverse=Fales)
- 说明: key函数用来提供一个值,这个值将作为排序的依据
  示例:
```python
  L = [5, -2, -4, 0, 3, 1]
  L2 = sorted(L)  # [-4, -2, 0, 1, 3, 5]
  L2 = sorted(L, reverse=True) # [5, 3, 1, ...]
  L2 = sorted(L, key=abs)   #[0, 1, -2, 3, -4, 5]
  names = ['Tom', 'Jerry', 'Spike', 'Tyke']
  sorted(names)
  sorted(names, key=len)
```


练习:
  1.用filter函数将1~100之间的所有素数prime放入到列表中并打印
  2. 用递归方式计算1+2+3+....+n的和
    def mysum(n):
        .... # 此处自己实现
  3. 用函数式编程,算出 1~20的阶乘的和
     1!+2!+3!+4!+5!+6!+7!+....20!
  4. 改写之前学生信息的程序
    每个人的信息有:
      姓名:name
      年龄:age
      成绩:score
    输入5个学生的信息.然后做如下操作:
    1)按成绩从高至低打印学生信息
    2)按年龄从高至低打印学生信息
    3)按年龄从低至高打印学生信息
    4)按原来输入顺序打印学生信息(要保持原列表不变)

## lambda 表达式 (又称匿名函数)

- 作用:
  创建一个匿名(无名)函数对象    
  同def类似,但不提供函数名

-语法:
lambda [参数1, 参数2, ....] : 表达式

注:[]内的部分表示可以省略

例:
```python
def myadd(x, y):
    return x + y
# 可以改写为:
myadd = lambda x, y : x + y
print("20+30=", myadd(20, 30))
```
练习看懂如下代码:
```python
def operator(fn, x, y):
    return fn(x,y)

operator((lambda a, b: a+b), 100, 200)# 返回值是多少?
operator((lambda a, b: a*b), 100, 200)# 返回值是多少?
```

- 语法说明:

1. lambda只是一个表达式,它用来创建一个函数对象
2. 当lambda表达式执行(调用)时,返回的是冒号(:)后表达式的值
3. lambda表达式创建的函数只能包含一条语句
4. lambda比函数简单且可以随时创建和销毁
5. lambda 有利于减少程序的耦合度

练习:
写一个lambd表达式,求两个变量的最大值
```python
def mymax(x, y):
    ....
mymax2 = lambda.....
print(mymax2(100, 200))  # 200
```

内置不可变数据结构

为了避开边界效应，不可变的数据结构是函数式编程中不可或缺的部分。不可变的数据结构保证数据的一致性，极大地降低了排查问题的难度。 
例如，Python中的元组(tuple)就是不可变的，所有对元组的操作都不能改变元组的内容，所有试图修改元组内容的操作都会产生一个异常。 
函数式编程语言一般会提供数据结构的两种版本（可变和不可变），并推荐使用不可变的版本。


递归
	递归是另一种取代循环的方法。

递归函数 recursion
  函数直接或间接的调用自身

示例:
def f():
    print("hello")
    f()

f()  # 调用函数
print("递归完成")

- 说明:

递归一定要控制递归的层数,当符合某一条件时要终止递归调用

几乎所有的递归都能用while循环来代替

- 优缺点:

优点:可以把问题简化,让思路更清晰,代码更简洁

缺点:递归因系统环境影响大,当递归深度太大时,可能会得到不可预知的结果

示例：（functional_programming/myfac_recursion.py）
计算阶乘:
   循环实现
```python
def myfac(n):
    r = 1
    for x in range(1, n+1):
        r *= x
    return r

print("5的阶乘是:", myfac(5))
```
用递归实现:
  5! = 5*4!  # myfac(5):  5*myfac(4)
  5! = 5*4*3! # myfac(5):  5*4*myfac(3)
  5! = 5*4*3*2!
  5! = 5*4*3*2*1!
  5! = 5*4*3*2*1
  5! = 5*4*3*2
  5! = 5*4*6
  5! = 5*24
  5! = 120