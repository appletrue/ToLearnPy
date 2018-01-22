面向对象思想的特征:
    1. 封装
    2. 继承(派生)
    3. 多态

==========================================================

# 封装 enclosure

- 作用:封装是指隐藏类的实现细节,让使用者不关心这些细节.

注:Python的封装是假的(模拟的)封装

- 私有实例变量和方法:
  Python类中,以双下划线"__"开头,不以双下划线结尾的标识符为私有成员

私有成员分为:**私有属性和私有方法**

私有成员在子类和类外部无法访问

示例：encloure01.py
```python
class A:
    def __init__(self, args):
        print("开始初始化了")
        self.__p = args

    def __private_method(self):
        print("你好,我是私有方法:")

    def showA(self):
        print("self.__p=", self.__p)
        self.__private_method()

#私有方法可以在类内部调用
a = A(100)
a.showA()
#输出结果如下：
开始初始化了
self.__p= 100
你好,我是私有方法:

# 私有方法不能在类外部调用
#err:   a.__private_method()
# 私有属性不能在外部使用
#err:   a.__p -= 2
#err:   print(a.__p)
```

# 继承(inheritance)　和 派生 (derived)

- 什么是继承/派生

- 为什么继承／派生
  继承的目的是延续旧的功能
  派生的目的是在类旧类的基础上添加新的功能

- 作用：用继承派生机制，可以将一些共有功能加在基类中，实现代码共享.在不改变超类的代码的基础上改变原有功能

- 名词:
  基类(base class) / 超类(super class) / 父类(father class)
  派生类(derived class) / 子类(child class)

- 单继承的语法：
     class 子类名(超类名):
       ...

示例：human.py
```python
class Human:
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    # def infos(self):
    #     print("我叫:", self.name,
    #           "我今年:", self.age, "岁")
    def say(self, what):
        print("说:", what)

    def run(self, speed):
        print("正在以", speed, "km/h速度奔跑!")

h1 = Human()
h1.say("天气真好!")
h1.run(5)


class Student(Human):
    # def say(self, what):
    #     print("说:", what)

    # def run(self, speed):
    #     print("正在以", speed, "m/分钟速度奔跑!")

    def study(self, prog):
        print("正在学习", prog)

s1 = Student()
s1.say("午餐咱们吃什么")
s1.run(7)
s1.study("Python3")


class Teacher:
    def techer(self, language):
        print("老师正在教:", language)

t1 = Teacher()
t1.techer("英文")

print("Teacher类的基类", Teacher.__base__)
print("Student类的基类", Student.__base__)
print("object类的基类", object.__base__)

t1.__class__.__base__
```

### 继承说明：

任何类都直接或间接的继承自object类。 object类是一切类的超类

`__base__`属性

作用：用来记录此类的基类(类实例)

super函数
  super(type, obj) 返回绑定超类的实例(要求obj必须为type类型的实例)
  super()  返回绑定的超类的实例,等同于(class, 实例方法的第一个参数),此方法必须用在方法内部

作用:
  返回绑定超类的实例,用超类的实例来调用其自身的方法

示例见: super.py
```python
class A(object):
    def hello(self):
        print("A类的hello(self)")


class B(A):
    def hello(self):
        print("B类的Hello(self)")

    def super_hello(self):  # 此方法用来调用基类的hello方法
        # super(B, self).hello()
        # 以上可以简写为:
        super().hello()

b = B()
b.hello()  # 调用B类的方法
# 调用基类方法:
super(B, b).hello()  # A类的hello 被调用 等同于 B.__base__.hello(b)
```

用于类的函数:

issubclass(cls, 类 或 类元组) 判断一个类是否是继承自其它的类,如果此类cls是类(class) 或 元组中的一个派生子类,则返回True, 否则返回False

示例:
class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(B):
    pass

issubclass(C, A)  # True
issubclass(C, B)  # True
issubclass(A, C)  # False
issubclass(C, D)  # False


查看:
  >>> help(__builtins__) 可以查看所有内建类的帮助



显式调用基类的构造方法:
  def __init__(self, ....):
      ....



## 多继承 multiple inheritance

多继承是指一个子类继承自两个或两个以上的基类

### 继承的语法:
```python
class 子类名(超类名1, 超类名2, ...):
      ...
```
示例见:multi_inherit01.py
```python
class Car:  # 汽车类
    def run(self, speed):
        print("汽车以", speed, "km/h的速度行驶")


class Plane:  # 飞机类
    def fly(self, height):
        print("在海拔", height, "米高度飞行!")


class PlaneCar(Car, Plane):
    """  PlaneCar类 同时继承自汽车和飞机"""

pl = PlaneCar()
pl.fly(10000)
pl.run(250)
```
当多个父类中拥有相同属性时，子类中使用时按照“广度优先”顺序搜索。（python2.2以前是深度优先）

示例：multi_inherit03.py
```python
class A(object):
    def foo(self):
        print('A foo')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A,B):
    pass

class C2(A,B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass 

if __name__ =='__main__':
    print (D.__mro__)   #新式类有__mro__属性，告诉查找顺序是怎样的
    d=D()
    d.foo()
    d.bar()
```
##执行的结果为：
```
(<class '__main__.D'>, <class '__main__.C1'>, <class '__main__.C2'>, <class '__main__.A'>, <class '__main__.B'>, <type 'object'>)
```

A foo （实际上搜索顺序为D=>C1=>A）
    			B
    	C2  A
    			B	
C2 bar（实际上搜索顺序为D=>C1=>C2）


### 多继承的问题(缺陷)
  标识符冲突的问题
  要谨慎使用多继承


## 多态 polymorphic

- 什么是多态: 
  字面意思 "多种状态"。多态是指在有继承/派生关系的类中,调用基类对象的方法,实际能调用子类的覆盖方法现象叫多态

### 覆盖 override(也叫重写 overwrite)

- 什么是覆盖

覆盖是指有继承关系的类中，子类中实现了与基类（超类)同名的方法，在子类实例调用该方法时，实际调用的是子类中的覆盖版本，这种现在叫做覆盖．

- 子类对象显示调用基类方法的方式：基类名.方法名(实例, 参数)

- 多态调用的方法与对象相关,不与类型相关

示例见:poly.py
```python
class Shape:  # 图形类
#    def draw(self):
#        self.drawSelf()
    def drawSelf(self):
        pass


class Point(Shape):
    def drawSelf(self):
        print("正在画一个点!")


class Circle(Point):
    def drawSelf(self):
        print("正在画一个圆")

#ok:
s = Shape()
#err:
#s.drawSelf()

shape = Point()
shape.drawSelf()

shape = Circle()
shape.drawSelf()
```

### 抽象类

不能实例化，只用于派生的类叫做抽象类。

### （纯）虚函数

拥有（纯）虚函数的类为抽象类。
​	
示例：pure_virtual.py
```python
from abc import ABC, abstractmethod  
  
class Base(ABC):  
    def __init__(self):  
       pass  

    @abstractmethod  
    def get(self):  
        print("Base.get()")  
        pass  
  
class Derive1(Base):  
    def get(self):  
        print("Derive1.get()")  
   
class Derive2(Base):  
    def get(self):  
        print("Derive2.get()")
  
if __name__ == '__main__':  
#    b = Base()  
#    b.get()  
    d1 = Derive1()
    d1.get()
    d2 = Derive2()
    d2.get()
```