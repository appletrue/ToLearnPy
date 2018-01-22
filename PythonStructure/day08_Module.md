# 模块 Module

## 什么是模块

模块是一个包含有一系列变量，函数，类等组成的程序组.  
模块是一个文件，模块文件名通常以.py结尾

  	`*.py --> *pyc --> *pyo -->pvm
  	*.c --> *.i --> *.s -->*.o --> bin`

- 作用：

让一些相关的变量，函数，类等有逻辑的组织在一起，让逻辑结构更加清晰    
模块中的变量，函数和类等可供其它模块或程序使用

- 分类:

1. 内置模块(builtins), 在解析器的内部可以直接使用
2. 安装的标准库模块,安装Python时已安装具可直接使用
3. 第三方模块(通常开源),需要自己安装
4. 用户自己编写的模块(可以作为其它人的第三方模块) 

- help(obj) 函数，可以查看模块相关的文档字符串

- dir(obj) 函数，返回模块所有属性的字符串列表

## 模块的导入

### import 语句

- 语法:　　import 模块名1 [as 模块新名1], 模块名2 [as 模块新名2], ...
- 示例：
```python
import math
import sys, os
```
- 作用：将某模块整体导入到当前模块
```python
import 语句用法
   模块名.属性名
math.sin(3.14)
```

### from import 语句

- 语法:
  from 模块名 import 模块属性名1 [as 属性别名1], 模块属性名2 [as 属性别名2], ...

- 作用：
  将某模块内的一个或多个属性导入到当前模块

- 示例：
```python
from math import sin
from math import pi
from math import factorial as fac
```

### from import * 语句

- 语法:  from 模块名 import *

- 作用：将某模块的所有属性导入到当前模块

- 示例：
```python
from math import *
sin(pi/2)  # 1.0
```

### dir()函数

dir([对象])  返回一个字符串列表

- 作用：
  如果没有参数调用,则返回当前作用域内的所有变量的列表

如果给定一个对象作为参数,则返回这个对象的所有变量列表

- 对于模块，返回这个模块的全部变量
- 对于类，返回类对象的所有变量
- 对于其它对象，返回所有变量，类变量和基类变量

## 自定义模块的编写
例：file : mymod.py

```python
def fac(n):
	print("正在计算n的阶乘...")
def sum_fac(n):
	print("正在计算阶乘的和...")
file test_mymod.py
import mymod
mymod.fac(20)
mymod.sum_fac(30)
```

## 模块的搜索路径:

import 模块名 # 对应 模块名.py 去哪儿找

- 查找的顺序

1. 搜索内置模块  
   sys.builtin_module_names 

2. sys.path提供的路径

3. 搜索程序运行时路径(当前路径)

-- PYTHONPATH 环境变量

此环境变量的值会在Python3的解析器启动时自动加载到 sys.path列表中

`$ export PYTHONPATH=$PATHONPATH:/home/smart`

Linux/Unix 用命令 printenv来查看所有的环境变量

模块的加载过程：

1. 在模块导入时，模块内的所有语句会执行
2. 如果一个模块已经导入，则再次导入时，不会重新重新执行所有的语句

模块化编程的优点：

1. 有利于多人开发
2. 使代码更加易于维护
3. 提高代码的复用率
4. 模块化编有助于解决函数名和变量名冲突问题

###  模块的属性:

#### 1、`__name__ `属性:

用来记录模块自身的名字

1.对于被导入模块,模块名为去掉路径前缀和".py"后缀的文件名
2.对于被执行的主模块,模块名为'__main__'

作用:

1. 记录模块名
2. 用来判断是否为主模块

#### `__doc__ `属性

用来绑定模块的文档字符串
模块的文档字符串是模块中第一行出现的没给赋值给变量的字符串

#### `__all__ `属性

- 作用:
  当用from import *语句导入模块时,只导入 __all__ 列表内的变量(属性)

`__all__`属性是用来存放可导出属性的列表

#### `__file__ `属性

 `__file__`用来记录模块对应的文件路径名

## 模块的隐藏属性

模块中以_ 或 __ 开头,不以__结尾的属性,在用from import * 语句导入时,将不被导入到其它模块

# 包(模块包) package

### 包的定义:

  包是将模块以文件夹的组织形式进行分组管理的方法

### 包的作用：

　将一系列模块进行分类管理，有利于防止名字冲突
　可以在需要时加载一个或部分模块而不是全部模块

示例：

```
 　　mypack/

    __init__.py
    menu.py
    games/
        __init__.py 
        contra.py
        supermario.py
        tanks.py
    office/
        __init__.py 
        excel.py
        word.py
        powerpoint.py
```

### 包的加载

```python
  import 包名 [as 包别名]
  import 包名.模块名 [as 模块别名]
  import 包名.子包名.模块名 [as 模块别名]
  ...

  from 包名 import 模块名 [as 模块新名]
  from 包名.子名包 import 模块名 [as 模块别名]
  from 包名．模块名 import 变量名 [as 变量别名]
  ...
  from 包名 import *
  from 包名.模块名 import 
  ……
```

包内的 __init__.py文件
  作用：
  　　在包被加载时自动调用.

1. 在内部填写包的文档字符串
2. 加载此包所依懒的一些模块或其它包

`__init__.py`内的__all__属性
作用：
　　用来记录哪儿些包需要导入
  当用 from 包 import *语句导入模块时，只查找__all__中所列出的模块

`__all__`属性只在from import *语句中起作用

包的加载路径：
　　同模块相同，设置方法：
1.可以设置　sys.path

2.可以设置 PYTHONPATH　环境变量

# 面向对象编程

面向对象是思想:

这是一种编程范式（常见编程范式有命令式，声明式（分领域特定和函数式），面向对象编程，泛型计算，元编程，默认并发，拼接式，符号式，基于知识，多范式）

  语法原生支持此思想的语言有: C++/Java/Python/Swift/C#....

​	c语言也可以实现面向对象编程，只是实现过程教复杂，不直接。
​	现代编程语言更倾向于多范式。

## 什么是对象

一切皆对象
对象拥有性质和行为（对应成员变量和成员方法），统称为属性。

### 两个概念:

#### 类 class

类是对拥有相同属性和行为的一类对象的抽象描述。

#### 对象(object) / 实例(instance)

对象是类的实例。

类和对象的关系，比如别墅设计图纸和一座具体的别墅。
所有按照这张图纸盖的别墅都是对象，具体到某一座别墅时，该别墅就是一个实例。

## 类的创建语法:

### class 类名 (继承列表):

'类文档字符串'
实例方法(类内的函数method)定义
类变量(class variable)  定义
类方法(@classmethod)    定义
静态方法(@staticmethod) 定义

注:[]的内容可以省略

类的作用:
  可以用类来创建对象(实例)
  类内定义的变量和方法能被此类所创建的所有实例共同拥有
  类通常用来创建具有共同属性的对象(实例)

最简单的类:

```
class Dog:
	pass
```

### 实例创建的表达式:

  类名([创建传参])
作用:
  创建一个类的实例对象并返回此实例  
实例说明:
  实例有自己的作用域和名字空间,可以为实例添加变量(属性)  
  实例可以调用类中的方法  
  实例可以访问类中的类变量

实例创建语法：
实例名 = 类名() 

示例：

```
class Dog:
	pass
d = Dog()
```

实例变量

```
一个实例化对象的成员变量。
定义语法：
self.变量名	#一般是在__init__函数中定义，赋值通过实参传递。
```

 调用语法:   实例.变量名
 在模块中调用:

```
模块名.实例.变量名
```

示例:（instance_var/dog.py）

```
class Dog:
"""这是一种小动物的定义
这种动物属于犬科
"""
def __init__(self,k,c,a):
	self.kinds=k
	self.color=c
	self.age=a
d1 = Dog("京巴", "白色", 1)
print d1.kinds, d1.color, d1.age
d2 = Dog("金毛","黄色",2)
print d2.kinds, d2.color, d2.age
```

实例方法:
语法:

```
class 类名(继承列表):
def 实例方法名(self, 形式参数1, 形式参数2, ...):
    "文档字符串"
    语句....
```

说明:
  实例方法是实质是函数,是定义在类内的函数  
  实例方法属于类的属性  
  实例方法的第一个参数代表调用这个实例方法的对象,一般命名为"self"  
  实例方法如果没有return语句,则返回None  

实例方法的调用语法:
  实例.实例方法名(调用参数)  
  或  
  类名.实例方法名(实例,调用参数)

示例：（instance_method/dog.py）

```
class Dog:
def __init__(self, k, c):
    self.kinds = k
    self.color = c

def setKinds(self, k):
    self.kinds = k

def setColor(self, c):
    self.color = c

def info(self):
    print("品种:", self.kinds,
          "颜色：", self.color)
dog1 = Dog("京巴", "黄色")
dog1.info()
dog1.setColor("白色")
dog1.info()
```

示例：（instance_function/）

```
class Dog:
"""这是一种小动物的定义
这种动物属于犬科
"""
def	__init__(self,k, c, a):
	self.kinds = k
	self.color = c
	self.age = a

def say(self):
	print("旺!")

def eat(self, that):
	"为狗进食,同时在food属性记住吃的是什么"
	print("小狗正在吃:", that)
	self.food = that

def food_info(self):
	""" 显示小狗的进食信息"""
	print("小狗刚吃过的是:", self.food)

def run(self, speed):
	print("小狗以", speed, "公里/小时的速度奔跑")

def get_color(self):
	return self.color
dog1 = Dog("京巴","白色",1)
print(dog1.get_color())
print(dog1.color )
dog1.say()     # 用对象来调用
Dog.say(dog1)  # 对类来调用
dog1.eat("骨头")
print(dog1.food)  # "骨头"
dog1.food_info()  # 小狗刚吃过的是: 骨头
#创建第二个小狗对象
dog2 = Dog("黑贝","黑色",2)
dog2.say()
dog2.eat("狗粮")
dog2.food_info()
dog1.run(23)
dog2.run(30)
```

### 构造方法:

作用:  创建对象时初始化实例变量
语法:

```
 def init(self[,形式参数列表]):
 	语句...
```

说明:

1. 构造方法名必须为　__init__　不可改变
2. 在一个类中只能有一个__init__构造方法(有多个时，最后一个起作用)
3. 构造方法会在实例创建时自动调用，且将实例自身通过第一个参数self传入__init__方法
4. 构造方法如果没有return 语句,则返回self自身

析构方法:

```
class 类名:
	__del__(self):
      pass
```

析构方法会在对象销毁时被自动调用;python语言不建议在对象销毁时做任何事情，因为该方法的调用时间难以确定

### 预置实例属性:

`__dict__`属性：  每一个对象(实例)都有一个`__dict__`属性，  __dict__属性绑定一个存储此实例自身属性的字典

`__doc__`属性：  用于保存类的文档字符串,用于help()中显示，  实例的文档字符串和类的文档字符串相同

`__class__ `属性：  `__class__`属性绑定创建此对象(实例)的类对象（类实例）

作用：

1. 可以借助于此属性来创建同类的实例   
2. 可以借助于此属性来访问类变量

`__module__`属性： 绑定此实例所属的模块
 在主模块中，此值为'__main__'； 不在主模块中，此值为模块名

示例：（instance_property/dog.py）

```
class Dog:
"""这是一种小动物的定义
这种动物属于犬科
"""
kinds=""
color=""
age=0
d = Dog()
d.kinds = "京八"
d.color = "white"
d.age = 1
print(d.kinds, d.color, d.age)
print("class:",d.class)
print("dict:",d.dict)
print("doc:",d.doc)
print("module:",d.module)
```

练习:
自己定义一个类Human(人类)
  有两个属性:

```
姓名(name)
年龄(age)
```

  有三个方法:

```
设置姓名(setName)  # 添加和修改姓名
设置年龄(setAge)   # .....
显示信息(infos)    # 显示人的信息
```

用此类来创建两个对象:

```
张三,20岁
李四,21岁
```

调用方法设置和显示信息

练习：
　　创建一个车类(Car)类
  车有属性:

```
品牌 brand
型号 model
颜色　color
```

  车的方法有:

```
run(speed)       # 以多少公里的速度行驶
infos()          # 显示信息
change_color(c)  #改变颜色　
```

例：
a4 = Car("红色", "奥迪", "A4")
a4.run(199)  # 红色奥迪A4正在以199km/h的速度行驶
a4.change_color("黑色")

a4.run(230)  # 黑色奥迪A4正在以230km/h的速度行驶

### 类变量

1. 是指在类class 内定义的变量，此变量属于类，不属于此类的对象(实例)
2. 类变量, 可以通过该类值接使用
3. 类变量，可以通过类的实例直接访问
4. 类变量可以通过此类的对象的__class__属性间接访问

例:

```
class Human:
home = "地球"
def __init__(self, name):
    self.name = name
print(home)  # 错的
print("Human.home:",Human.home)  # "地球"
h1 = Human("张三")
print("h1.home:",h1.home)  # 访问类对象
h1.home = "火星"  # 为此对象添加了实例属性
print("h1.home:",h1.home)  # 火星 访问实例属性
print("Human.home:",Human.home)  # 访问类属性
print("h1.class.home:",h1.class.home)  # 间接访问类变量
h1.class.home = "月球"
print("Human.home:",Human.home)
h2 = Human("李四")
print("h2.home:",h2.home)  # 月球
```

### 类方法 @classmethod

-   类方法是只能访问类变量的方法
-   类方法需要使用@classmethod装饰器定义
-   类方法的第一个参数是类的实例,约定写为cls

说明:
  类实例和对象实例都可以调用类方法  
  类方法不能访问实例变量

示例见: (class_method/classmethod.py)


```
class ICBC:
moneys = 10000000  # 壹仟孺
@classmethod
def total_money(cls):
    print("工商银行总资金数:", cls.moneys)

def __init__(self, b):
    self.branch = b
    self.money = 5000000
    self.__class__.moneys -= 5000000

def address(self):
    print("地址为:", self.branch)
ICBC.total_money()
b1 = ICBC("中关村支行")
b1.total_money()
```

——类方法和实例方法对比:

1. 类方法能够访问类变量,不能访问实例变量  
   实例方法能够访问类变量,也能访问实例变量
2. 类方法可以用实例来调用,也可以用类来调用  
   实例方法在调用时必须传入实例.

### 静态方法 @staticmethod

  静态方法是普通的函数  
  静态方法定义在类的内部,只能凭借该类和实例调用  
  静态方法需要使用@staticmethod装饰器定义  
  静态方法与普通函数定义相同,不需要传入self实例参数和 class类参数  
说明:  
  类实例和对象实例都可以调用静态方法   
  静态方法不能访问类变量和实例变量

示例:

```
class A:
@staticmethod
def myadd(a, b):
    return a + b
print(A.myadd(100, 200))
a = A()
print(a.myadd(300, 400))
```

——实例方法,类方法,静态方法总结:
不想访问类变量和实列变量(属性),用静态方法  
只想访问类内变量,不想访问实例属性用类方法  
即想访问类内变量,也想访问实例变量用实例方法   



### 特性属性 @property

  用来模拟一个属性
  通过@property 装饰器可以对模拟属性赋值和取值加以控制
  实现其它语言所拥有的 getter 和 setter功能

示例见: circle.py
class Circle:  # 圆类

```
def __init__(self, r):
    self.radius = r  # 半径

@property
def area(self):  # 面积
    print("area 函数被调用...")
    return math.pi * self.radius ** 2

@area.setter
def area(self, a):  # a代表面积
    self.radius = math.sqrt(a/math.pi)
    print("面积更改")
c1 = Circle(10)
print(c1.area)
print
c1.area = 31415.926
print(c1.radius)
print(c1.area)
```

### 类的 __slots__ 属性

作用:

1. 限定一个类创建的实例只能有固定的实例属性；不允许对象添加列表以外的实例属性  
2. 防止用户因错写属性名称而发生程序错误

说明:
  __slots__属性是一个列表,列表的值是字符串；  
  含有__slots__属性的类所创建的实例对象没有__dict__属性,即此实例不用字典来存储属性.

示例见:slots.py

对象的属性管理:
函数
  getattr(obj, name [,default]) 从一个对象得到对象的属性,getattr(x, 'y')等同于x.y;
  当属性不存在时,如果给出default参数,则返回default,如果没有给出default则产生一个AttributeError错误
  hasattr(obj, name) 用给定的name返回对象obj是否有此属性,此做法可以避免getattr()函数引发错误
  setattr(obj, name, value) 给对象obj的名为name 的属性设置相应的值, set(x, 'y', v) 等同于x.y = v
  delattr(obj, name) 删除对象obj的name属性, delattr(x, 'y')等同于 del x.y

示例:

```
class MyClass:
	pass
obj = MyClass
obj.a1 = 100
setattr(obj, "a2", 200)
print(obj.dict)
print(hasattr(obj, "a2"))
print(hasattr(obj, "a3"))
print(getattr(obj, 'a2'))
print(getattr(obj, 'a3', 0))
del obj.a2
delattr(obj, 'a1')
print(obj.dict)
```

用于类的函数:
  isinstance(obj, 类或类的元组) 返回这个对象obj是否为某个类或某些类的对象,如果是返回True,否则返回False
  type(obj) 返回对象的类型

示例:

```
class A:
	pass
 a = A()
 def fn(x):
# 我们不知道x绑定是什么类型 ??
  if isinstance(x, A):
      print("x是一个A类型的对象")
  elif isinstance(x, int):
      print("x为整数")
  fn(1)
  fn(a)
  fn([1,2,3])
  if type(a) == A:
 print("a是A类型的对象")
```

 id函数
  id(obj) 返回对象的标识(identity)



练习:

1. 自己写一个类Student, 此类的对象有属性name,age,score 用来保存学生的姓名,年龄,成绩, 用input读入5个学生关相信息,用对象来存储这些信息(不用字典), 打印五个学生信息

练习:

```
1. 写一个正方形类:
 有三个属性:
    边长 length
    周长 ...
    面积 area
 用此类生成对象,此三个属性其中一个变量,所有属性同步变化
注:用特殊属性@property实现
```

1. 修改学生管理程序,用来对象存储学生信息.
   每个学生有infos()方法,用于显示学生信息

   L = []
   for i in range(5)

   ```
   n = "zhangsan"
   a = 21
   s = 89
   stu = Student(n, a, s)
   L.append(stu)
   ```

   +----+----+----+
   | 姓名| 年龄|成绩|
   +----+----+----+
   for x in L:

   ```
   x.infos()

   ```

   +----+----+----+