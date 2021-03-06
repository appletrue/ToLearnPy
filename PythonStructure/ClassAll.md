# 类

------
1. 新式类(object类)和旧式类
2. 类和实例
3. 命名空间
4. 继承
5. 多态
6. 类方法和静态方法
7. 特殊(魔法)属性和方法
8. @property
9. 元类
----------------

Python面向对象特性中最核心的一部分就是类了，花了点时间整理了一下，做成笔记，方便日后翻阅。

## 新式类(object类)和旧式类

### 1.1 定义

- 旧式类：

定义一个旧式类A:

```
class A:
    pass
```

实例化:

```
a = A()
```

- 新式类：

定义一个新式类B:

**方法一**：

```
class B(object):  # B类继承object类，括号表示继承关系
    pass          # 在Python3中所有的类都默认为新式类，不需要再显式指定了
```

**方法二：**

在类的前面加上一句`__metaclass__ = type`，就不需要在类名字后面加上`(object)`了：

```
__metaclass__ = type
class B:
    pass
```

### 1.2 区别

在Python中，万物皆对象。因此，类也有类，类的类叫**元类**（这里强调的是实例化过程）。

- 在旧式类中，类源自于`classobj`，类的实例则源自于`instance`。对旧式类的实例`x`，`x.__class__`查看的才是它对应的类，但`type(x)`查看的结果永远是`<type 'instance'>`

```
class C():
    pass
c = C()
print type(C)  # <type 'classobj'>
print type(c)  # <type 'instance'>

print C  # __main__.C
print c  # <__main__.C instance at 0x101dfd050>
print c.__class__  # __main__.C
```

- 引入新式类的目的是为了用`元类`来构造类对象，统一类的模型。在新式类中，所有的类都继承自`object`，都是`type`的实例。新式类才是真正的类。在新式类中，`x.__class__`和`type(x)`的结果是一样的（它们强调的都是实例化关系）。在新式类中，**一般**类的元类是type类（因此指定了`__metaclass__ = type`的类就是新式类，继承自`object`)。

```
class CC(object):
    pass
cc = CC()
print type(CC)  # <type 'type'>
print type(cc)  # <class '__main__.CC'>

print CC  # <class '__main__.CC'>
print cc  # <__main__.CC object at 0x10f7aa290>
print cc.__class__  # <class '__main__.CC'>
```

## 2. 类和实例

### 2.1 self的作用

举个简单的例子：

```
__metaclass__ = type
class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
```

实例化：

```
girl = Person('chen')
name = girl.getName()
print 'the person's name is: ',name
```

- 在类内部，所有的传入数据都赋值给一个变量，这个变量是self。在类中定义的函数的第一个参数都是self，就是起到这个作用—接收实例化过程中传入的所有数据。
- self是一个实例，准确来说，是**实例的引用变量**。
- 在初始化函数`__init__`中通过`self.attribute`的方式，规定self实例对象的属性，这个属性也是类实例化对象的属性。

### 2.2 类属性和实例属性

类也是一个对象，它也有属性

```
class A(object):
    x = 7
foo = A()  # 实例化
```

1. 在类中，变量x引用的数据可以通过类来直接调用：`A.x`，这就是**类属性**。

2. `foo.x`叫**实例属性**。

3. 对于**不可变数据**，**实例属性无法更改类属性，但是类属性可以更改实例属性**。

   解释：这句话表述不太好。对`foo.x`进行数学运算并不会更改`A.x`的值。若只是调用`foo.x`而不对x进行运算等操作，`foo.x`就**完全**等同于`A.x`，这里得完全指的是同一个内存地址。一旦对`foo.x`进行操作，本质是实例foo又建立了一个新的属性x，此时再更改`A.x`的值就不会影响`foo.x`了。

4. 当类中变量引用的是**可变数据**，情况会有所不同。因为可变数据能进行原地修改。

   如：

   ```
   class B(object):
       y = [1,2,3]
   bar = B()
   ```

   这种情况下B.y和bar.y始终保持**完全等同**。

### 2.3 访问限制

在属性或者方法的名称前面加上两个下划线，即`__`，即可将之私有化，使不能被外部访问。

```
class A(object):
    def __init(self, name):
        self.__name = name
```

此时尝试从外部访问会出错：

```
a = A()
a.__name  # AttributeError: 'A' object has no attribute '__name'
```

若要从外部访问或修改私有变量，建议如下操作：

```
class A(object):
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
```

之所以是建议，是因为以双下划线开头的变量并不是不能从外部访问。不能从外部访问`__name`是因为Python解释器对外把`__name`改成了`_A__name`。因此，仍然可通过`_className__attr`的形式访问私有变量。

另外，如果变量名前面只有一个下划线`_`，表示不要`随意访问这个变量`，虽然它可以直接被访问。

### 2.4 获取对象信息

当我们拿到一个对象，常用的有如下几种方法考察它的类型和方法:

- 使用`type`

  用`type(obj)`查看对象的类型（为何的实例）：

  ```
  a = A()
  print type(a)  # <class '__main__.A'>
  ```

- 使用`isinstance`

  使用`isinstance(obj, type)`判断对象是否为指定的type类型的实例：

  ```
  isinstance(a, A)  # True
  ```

- 使用`hasattr/getattr/setattr`（这些方法均不能访问私有属性）

  - 使用`hasattr(obj, attr)`判断对象是否具有指定属性/方法；
  - 使用`getattr(obj, attr[, default])`获取属性/发法的值，若没有找到对应的属性值则返回default值（前提是设置类default），否则会抛出`AttributeError`异常；
  - 使用`setattr(obj, attr, value)`设定该属性/方法的值，类似于`obj.attr = value`;

- 使用`dir`

  使用`dir(obj)`可以获取相应对象的**所有**属性和方法名的列表：

  ```
  class A(object):
      def __init__(self, name, age):
          self.__name = name
          self.age = age

      def get_name(self):
          return self.__name

  a = A('yang', 22)
  print dir(a)
  # ['_A__name', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'get_name']
  ```

## 3. 命名空间

命名空间分为以下三类：

- **内置命名空间(Built-in Namespaces)**: Python运行起来，它们就存在。内置函数的命名空间都属于内置命名空间。

- **全局命名空间(Module: Global Namespaces)**: 每个模块创建它的全局命名空间，彼此独立，互不冲突。

- **本地命名空间(Functions&Class: Local Namespaces)**: 每个函数或类定义的空间就是本地命名空间。若函数返回了结果或者抛出异常，则本地命名空间结束。

  ```
  程序在查询上述三种命名空间的时候，按照从里到外的顺序，即：Local Namespaces --> Global Namesspaces --> Built-in Namesspaces

  ```

## 4. 继承

### 4.1 基本概念

继承很简单，注意，如果子类重写了父类的方法，父类的方法就被覆盖。

### 4.2 多重继承

```python
class K1(object):
    def foo(self):
        print "K1-foo"

class K2(object):
    def foo(self):
        print "K2-foo"
    def bar(self):
        print "K2-bar"

class J1(K1, K2):
    pass

class J2(K1, K2):
    def bar(self):
        print "J2-bar"

class C(J1, J2):
    pass

if __name__ == "__main__":
    print C.__mro__  # 打印出类的继承顺序Method Resolution Order
    m = C()
    m.foo()
    m.bar()
```

运行结果：

```python
(<class '__main__.C'>, <class '__main__.J1'>, <class '__main__.J2'>, <class '__main__.K1'>, <class '__main__.K2'>, <type 'object'>)
K1-foo
J2-bar
```

搜索顺序：**广度优先**。即C\==>J1\==>J2==>K1\==>K2

### 4.3 super函数

1.看例子：

```python
__metaclass__ = type
class Base:
    def __init__(self):
        self.a = 1
class Child(Base):
    def __init__(self):
        super(Child, self).__init__()  # 等价于Base.__init__ (self)
        self.b = 2
chen = Child()
print chen.a
```

(1) 若子类Child中没有定义`__init__`函数，则子类的实例chen就从父类的`__init__`函数中寻找a

(2) 若子类Child定义了`__init__`函数，但是没有super那一行，就会报错，因为子类重写了父类的`__init__`方法，父类的`__init__`方法就被覆盖掉了，因此无变量a

(3) 既要保留父类`__init__`中的参量又要新添加参量，就可以用super函数。super函数的第一个参数是当前子类的名字，第二个参数是self，然后是点号，后面是要调用的父类的方法

2.重点：**不要一说到 super 就想到父类！super 指的是 MRO 中的下一个类！**

例子：

```python
class Root(object):
    def __init__(self):
        print("this is Root")

class B(Root):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")
        
class C(Root):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")
        
class D(B, C):
    pass
        
d = D()
print(d.__class__.__mro__)
```

输出：

```python
enter B
enter C
this is Root
leave C
leave B
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.Root'>, <type 'object'>)
```

对于`super(B, self).__init__()`, 首先，我们获取`self.__class__.__mro__`，注意这里的self是D的实例而不是B的：`(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.Root'>, <type 'object'>)`. 然后通过B来定位MRO中的index，并找到下一个，也就是C，于是调用C的__init**, 打出enter C因此，`super(B, self).**init**()和Root.**init__(self)`是不一样的

3.这里我们在回头看看super内部是怎么实现的：

```python
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
```

super内部接收两个参数cls和inst。inst用来确定mro, 然后通过cls来定位mro中当前的index, 并返回mro中下一个值。

## 5. 多态

有了继承，才能有多态。多态就是指：**不同类型的对象对同一消息会做出不同的响应**。

事实上，我们经常使用到多态：

```
1 + 2      # 3
'a' + 'b'  # 'ab'
```

再举一个类的例子：

```python
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print 'Hello, I am %s.' % self.name

class Dog(Animal):
    def greet(self):
        print 'WangWang.., I am %s.' % self.name

class Cat(Animal):
    def greet(self):
        print 'MiaoMiao.., I am %s' % self.name

def hello(animal):
    animal.greet()
```

多态的使用：

```
dog = Dog('dog')
hello(dog)  # WangWang..., I am dog.

cat = Cat('cat')
hello(cat)  # MiaoMiao..., I am cat.
```

可以看到，`cat`和`dog`是两个不同的对象，对它们调用`greet`方法，它们会自动调用实际类型的`greet`方法，做出不同的响应，这就是多态。

## 6. 类方法和静态方法

对一个类，我们要调用它的一个方法，必须要绑定实例，而不能直接通过`类名.方法名()`的形式调用。因此，想要通过类来调用方法，而不是通过实例，可以使用**静态方法**`@staticmethod`和**类方法**`@classmethod`的形式实现。

二者的形式：

```
@classmethod修饰的方法的第一个参数必须是cls。cls指的是类的本身，若有继承出现，cls指当前类。
@staticmethod修饰的方法没有self和cls参数，可以不接受参数
```

使用情形：

考虑如下的Date类：

```
class Date(object):
    
    day = 0
    month = 0
    year = 0
    
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
```

如果我们有很多非标准格式的`day-month-year`(如11-09-2012)这样的数据，要将它们解析为Date所能接收的标准格式并创建类的实例该怎么做呢？

正常我们可以在类外添加额外代码处理：

```
day, month, year = map(int, string_data.split('-'))
data1 = Data(day, month, year)
```

这样将代码放在类外单独处理，固然可以，但是若能让类本身就能处理这种非标准输入不是更好吗？后者显然维护起来更方便。

用类方法实现如下：

在Date中加入这样一个类方法：

```
@classmethod
def from_string(cls, data_as_string):
    day, month, year = map(int, data_as_string.split('-'))
    rerurn cls(day, month, year)
    
data = Data.from_string('11-09-2012')
```

回头看我们的代码，我们将**数据预处理**封装在了类中，这样不仅好维护，没有代码扩散到类外的情况，而且更酷的是其子类也能继承这个类方法，也具有这个特性。

那静态方法呢？

假设有这样一个需求，对输入的数据进行有效性判断，怎么做呢？

再插入这样一个静态方法：

```
@staticmethod
def is_data_valid(data_as_string):
    day, month, year = map(int, data_as_string.split('-'))
    return day <=31 and month <=12 and year <=3999

# usage
is_data = Data.is_data_valid('11-09-2012')

```

同样没有进行实例化，直接把预处理封装在了类中。

那静态方法和类方法的区别在哪呢？区别就在类方法的第一个参数是`cls`，在继承时，`cls`指的是当前类而不是父类。也就是说，同样的类方法在不同的子类中可以有不同的表现，有点重载的意思。见下面的例子：

我们重写Date函数：

```
class Date:
  def __init__(self, month, day, year):
    self.month = month
    self.day   = day
    self.year  = year

  def display(self):
    return "{0}-{1}-{2}".format(self.month, self.day, self.year)

  @staticmethod
  def millenium(month, day):
    return Date(month, day, 2000)

```

使用：

```
new_year = Date(1, 1, 2013)                # Creates a new Date object
millenium_new_year = Date.millenium(1, 1)  # also creates a Date object. 

# Proof:
new_year.display()            # "1-1-2013"
millenium_new_year.display()  # "1-1-2000"

isinstance(new_year, Date)  # True
isinstance(millenium_new_year, Date)  # True

```

这时来了一个Date类的子类DateTime:

```
class DateTime(Date):
  def display(self):
      return "{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year)

```

使用：

```
datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)

isinstance(datetime1, DateTime)  # True
isinstance(datetime2, DateTime)  # False

datetime1.display()  # returns "10-10-1990 - 00:00:00PM"
datetime2.display()  # returns "10-10-2000"

```

显然`datetime2`是`Date`的实例而不是`DateTime`的实例。

很多情况下，我们并不希望是这样的结果，我们希望上面的`datetime2`按所在子类指定的形式显示。怎么做呢？使用类方法。将Date类的静态方法替换为下面的类方法：

```
@classmethod
def millenium(cls, month, day):
    return cls(month, day, 2000)

```

这时候再使用：

```
datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)  # 这里cls会指向DateTime

isinstance(datetime1, DateTime)  # True
isinstance(datetime2, DateTime)  # True

datetime1.display()  # "10-10-1990 - 00:00:00PM"
datetime2.display()  # "10-10-2000 - 00:00:00PM"

```

总结下：

- 静态方法其实就是一个定义在类中的方法，只是调用时可以不需要先对类进行实例化，直接用类调用即可。无论后面怎么继承，它的实现不变。
- 类方法也在调用时也不需要先对类进行实例化，但是它的实现，在继承时是跟随当前的子类的(因为它的第一个参数永远是cls)
- 它们常用于将数据预处理等封装在类内，避免代码扩散到类外不好维护。

## 7. 特殊(魔法)属性和方法

Python中以双下划线`__`开头和结尾的属性和方法，叫特殊属性(方法)或魔法属性(方法)。怎么读呢，比如`__init__`，推荐的读法是”dunder init dunder”(as suggested by Mark Jackson)。对魔法方法而言，其实它的意思是不需要**显式调用**，Python底层会自动调用它们。

### 7.1 属性

#### 7.1.1 __doc__

帮助说明，一般在定义类的时候以`'''说明'''`形式加的注释会以string的形式存在`__doc__`中

#### 7.1.2 __module__

对某个**函数**或者**实例对象**，查看它所在的模块的名字。比如新建了一个`test.py`文件，里面有一个实例`a`。若在`test.py`中直接运行`print a.__module__`，结果是缺省值`__main__`；如果在另一个文件中导入了`test.py`中的`a`，在另一个文件中运行`print a.__module__`，结果是`test`，也就是返回了不带后缀的文件名。

#### 7.1.3 __name__

返回所在模块的名字，一般**单独使用**，如`print __name__`。

与`__module__`相同，直接运行py脚本时，`__name__`被赋予缺省值`__main__`；一旦被其他文件或模块导入，那么以前的那个脚本的`__name__`值就变成了那个脚本的文件名（不带py后缀）

最常用的用法是，在某个py脚本如`test.py`最后添加：

```Python
if __name__ == '__main__':
    xxx
```

这样做的好处是，直接运行`test.py`，上面的`xxx`部分会执行。但是在其他地方`import test`再运行时，`xxx`就不会执行了（此时`test.py`中执行到`if`语句时，`__name__ = test`，不再是缺省值，当然不会执行`xxx`了）

#### 7.1.4 __class__

返回对象的类信息，也就是查看是谁的实例。顶层是`type`

#### 7.1.5 __base__

返回类的父类，顶层是`object`

#### 7.1.6 __dict__

字典，储存对象的属性。这里我们再回头理解2.2中的类属性和实例属性：

```python
class A(object):
    Q = 1
    def __init__(self, q):
        self.q = q

a = A(0)
```

查看a和A的属性：

```python
print a.__dict__  # {'q': 0}
print A.__dict__  # {'__module__': '__main__', 'Q': 1, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None, '__init__': <function __init__ at 0x1028156e0>}
```

看，虽然`a`可以访问`Q`，但是`a`的属性字典的key中并没有`Q`。因此这里的`a.Q`和`A.Q`是完全等同的，都指向的是`A`的`Q`属性。

这时，我们对a操作：

```python
a.Q = 1
print a.__dict__  # {'q': 0, 'Q': 1}
```

`Q`属性就添加到了`a`的属性字典中。本质就是按照`a.attr = val`的方式给`a`新添了一个属性。此时`a.Q`和`A.Q`就是两个完全不同的东西了，互不影响。

#### 7.1.7 __slots__

在Python中，当我们创建了一个类的实例后，我们还可以给该实例绑定任意新的属性或方法：

```python
class P(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
p = P()
p.z = 5
```

`__slots__`的作用：限定运行绑定的属性，目的是为了不浪费内存。

改进如下：

```python
class P(object):
    __slots__ = ('x', 'y')  # 只允许使用x和y
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
p = P()
p.z = 5  # AttributeError: 'P' object has no attribute 'z'
```

注意：`__slots__`设置的属性仅对当前类有效，对继承的子类不起效，除非子类也定义了`__slots__`

### 7.2 方法

#### 7.2.1 `__new__ 和 __init__`

在Python中，当我们创建一个类的实例时，其实是先调用`__new__(cls[, ...])`来创建实例，然后由`__init__(self[, ...])`方法再对该实例(self)进行初始化

有以下几点需要注意：

- `__new__`在`__init__`之前被调用
- `__new__`是类方法，`__init__`是实例方法
- 若重载`__new__`方法，需要返回类的实例

一般情况下，我们不需要重载 `__new__` 方法。但在某些情况下，我们想**控制实例的创建过程**，这时可以通过重载 `__new__`方法来实现。

举个例子：

```python
class A(object):
    _dict = dict()

    def __new__(cls):
        if 'key' in A._dict:
            print "EXISTS"
            return A._dict['key']
        else:
            print "NEW"
            return object.__new__(cls)

    def __init__(self):
        print "INIT"
        A._dict['key'] = self
```

执行情况：

```
>>> a1 = A()
NEW
INIT
>>> a2 = A()
EXISTS
INIT
>>> a3 = A()
EXISTS
INIT
```

#### 7.2.2 `__str__ 和 __repr__`

- `__str__`: 要**打印**出来的内容，也就是要`str()`出来的内容
- `__repr__`: 要**输出**来的内容（终端输出），很多时候可以让`__repr__ = __str__`

举个例子：

```python
class Foo(object):
    def __init__(self, name):
        self.name = name

foo = Foo('yang')
print foo  # <__main__.Foo object at 0x108963f10>
```

加上`__str__`函数：

```python
class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'name is %s' % self.name

foo = Foo('yang')
print foo  # name is yang
		   # 等价于调用print str(foo)

# 终端中
>>> foo  # <__main__.Foo object at 0x108963f10>
```

若要终端中也显示，需加上`__repr__`函数：

```
class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'name is %s' % self.name

    def __repr__(self):
        return 'name is %s' % self.name

foo = Foo('yang')

# 终端中
>>> foo  # name is yang
```

一般我们可以直接改写为`__repr__ = __str__`，直接让二者功能一致。

#### 7.2.3 __getattr__

`__getattr__(self, item)`：只在当调用**不存在**的属性attr时会调用此方法(类属性和实例属性中都没有):

```
class Foo(object):
    def __init__(self, name):
        self.name = name
        
    def __getattr__(self, item):
        if item == 'age':
            print 'no such attr!'
```

但是有一个问题，上面尝试调用实例的`age`属性会打印出`no such attr!`，但是调用其他不存在的属性如`gender`时, 会返回`None`，因为`__getattr__`默认返回的就是`None`。因此，为了让`__getattr__`只响应几个特定的属性，建议加入异常处理：

```
def __getattr__(self, item):
    if item == 'age':
        print 'no such attr!'
	raise AttributeError('Point object ha no attribute %s' % item)

```

**注意：**`__getattr__`并不会影响实例的`__dict__`属性。

#### 7.2.4 __setattr__

`__setattr__(self, name, value)`: 在尝试给属性赋值时调用此函数。name为属性名，value为要赋的值。简单说，给`__dict__`添加属性和值就是通过这个函数实现的。

看下面的例子：

```
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __setattr__(self, name, value):
        print 'call func setattr (%s, %s)' % (name, value)
        return object.__setattr__(self, name, value)

p = Point(1, 2)

```

输出的结果是：

```
call func setattr (x, 1)
call func setattr (y, 2)

```

整个的数据流转过程为：

先执行到`__init__`函数第一行，获取了实例的属性名字`x`和`y`，并让x=1，y=2。然后分两次转去调用`__setattr__`：第一次`name`为`x`，`value`为`1`，然后执行`object.__setattr__`函数，跳转到`__init__`中的`self.x = x`给实例`p`的`__dict__`添加属性–值这样的键值对；第二次`name`为`y`，`value`为`3`，最后执行`__init__`中的`self.y = y`。

**注意**：上面`return object.__setattr__(self, name, value)`等价于`self.__dict__[name] = value`。这里不能用`self.name = value`，因为这样会调用自己，然后陷入死循环，最后报错：`RuntimeError: maximum recursion depth exceeded`。

#### 7.2.4 __delattr__

`__delattr__(self, name)`:删除属性的值。`del obj.name`就是调用的这个方法

在上小节的代码中加入以下几行：

```
def __delattr__(self, name):
    return object.__delattr__(self, name)

```

这样执行`del p.x`就会执行上述代码。

#### 7.2.5 __getattribute__

`__getattribute__(self, name)`：无论name是否存在，只要name被访问，就一定调用此方法。

如果同时定义了`__getattr__`，除非`__getattribute__`抛出异常，否则不会调用`__getattr__`。

同样，为了避免死循环，`__getattribute__`中的实现应该用`return object.__getattribute__(self, name)`而不能用`return self.__dict__(name)`

#### 7.2.6 __call__

能让实例直接像函数一样调用，形如`x(arg1, arg2)`的方式，就是在调用`x.__call__(arg1, arg2)`。

```
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __call__(self, z):
        return self.x + self.y + z

```

使用如下：

```
>>> p = Point(3, 4)
>>> callable(p)     # 使用 callable 判断对象是否能被调用
True
>>> p(6)            # 传入参数，对实例进行调用，对应 p.__call__(6)
13

```

#### 7.2.7 `__iter__和next`

在某些情况下，我们希望实例对象可被用于 `for…in` 循环，这时我们需要在类中定义 `__iter__` 和 `next`（在 Python3 中是`__next__`）方法，其中，`__iter__` 返回一个迭代对象，`next`返回容器的下一个元素，在没有后续元素时抛出 `StopIteration`异常

以斐波那契数列为例：

```
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # 返回迭代器对象本身
        return self

    def next(self):  # 返回容器的下一个元素
        a = self.a
        self.a, self.b = self.b, self.a + self.b
        return a

fib = Fib()
print fib.next()
for i in fib:
    if i > 10:
        break
    print i
# 0 1 1 2 3 5 8

```

#### 7.2.8 `__getitem__、__setitem__、__delitem__`

格式：

```
__getitem__(self,var):可以使用obj[n]方式获取值,例如Fib函数可以取其中一项.如果使用list的切片功能,就要判断var是否slice对象isinstance(var,slice).slice有start, stop, step属性,负数处理要另外处理
__setitem__(self,var,value):可以用来对值进行赋值时的操作.
__delitem__(self,var):删除某个元素的操作.

```

总之，涉及到`obj[n]`的用法就与以上三个方法有关，它们分别是获取值，设置值，删除值

举个简单例子：

希望对上小节的斐波那契数列`Fib`使用`obj[n]`和切片的方式取值，进行如下改写：

```
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 0, 1
            for i in xrange(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            a, b = 0, 1
            start, stop = item.start, item.stop
            L = []
            for i in xrange(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L

fib = Fib()
print fib[3]   # 2
print fib[0:4] # [0, 1, 1, 2]

```

综合例子：设计一个Point类，它有一个坐标属性。既能用`obj[i]`赋值和调用，又能用`obj.x`和`obj.y`分别赋值和调用两个坐标值

```
class Point(object):
    def __init__(self, x=0, y=0):
        self.data = [x, y]

    def __str__(self):
        return "point(%s, %s)" % (self.data[0], self.data[1])

    __repr__ = __str__

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, idx, value):
        self.data[idx] = value

    def __delitem__(self, idx):
        del self.data[idx]

    @property
    def x(self):
        return self.data[0]

    @x.setter
    def x(self, x):
        self.data[0] = x

    @property
    def y(self):
        return self.data[1]

    @y.setter
    def y(self, y):
        self.data[1] = y


p = Point(2, 3)   # 
print p           # point(2, 3)
print p[0], p[1]  # 2 3
print p.x         # 2
p.x = 4
print p           # point(4, 3)

```

## 8. @property

`@property`可将方法变成属性。

比如有一个类P，其实例p，p有一个私有属性`_score`（不想暴露），若要调用`_score`或对其赋值，可以定义`get_score`和`set_score`方法。

其实还可以使用`property`将方法变成属性：

```
class P(object):

    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

p = P(1)
print p.score  # 像属性一样调用
p.score = 2    # 像属性一样直接赋值
print p.score

```

上面若只有`@property`，则`score`是只读属性。加上`setter`后才能赋值。

## 9. 元类

### 9.1 继承与实例化

在面向对象体系里面，存在两种关系：

- 继承关系：在python里面用`__base__`可查看，顶层是`object`
- 实例关系：表现为某个类型的实例化。在python里面用`__class__`查看，顶层为`type`。

```
>>> object.__base__  # 继承关系上object为顶层
None
>>> object.__class__  # object是type的实例
<type 'type'>

>>> type.__base__  # type继承自obect
<type 'object'>
>>> type.__class__  # type是type的实例
<type 'type'>

# python中type和object就像鸡和蛋的关系

>>> int.__base__  # int继承自object
<type 'object'>
>>> int.__class__  # int是type的实例
<type 'type'>

```

再看一个实例化的例子：

```
>>> class A(object):
... 	pass 
>>> a = A()
>>> a.__class__  # a是A的实例
<class '__main__.A'>
>>> a.__base__  # 报错。实例没有继承关系，所以没有__base__属性
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__base__'

```

### 9.2 type的用法

- `type(obj)`：获取对象的相应类型，与`obj.__class__`等同
- `type(className, (parents), {attr: value})`：创建并返回一个类，三个参数分别对应于类名(字符串)，父类(元组形式)，属性(字典形式)

因此以下两个语句等价：

```
class Integer(object):
    name = 'interger'
    def inc(self, num):
        return num + 1
#------------------------
# 父类元组为空，默认继承object
Integer = type('Integer', (), {'name': 'interger',
                                   'increase': lambda self, num: num + 1})

```

也就是说，类的定义过程，其实是**type类型实例化的过程**

### 9.3 元类metaclass

先总结下：

- 类的类就是元类（强调实例化），默认是type
- type是所有元类的**父亲**


- 在实例化时，也就是创建类型对象时，会按以下顺序查找`__metaclass__`属性：

`class.__metaclass__ -> bases.__metaclass__ -> module.__metaclass__ -> type`

理解以上几点，看下面例子：

```
>>> class M(type):
... 	pass
>>> M.__class__
<type 'type'>
>>> M.__base__  # 继承自type
<type 'type'>

```

上面的M就是一个元类。要实例化，可定义一个类：

```
>>> class TM(object):
... 	__metaclass__ = M  # 指定元类
>>> TM.__class__
<class '__main__.M'>
>>> TM.__base__
<type 'object'>

```

其实上面的`__metaclass__ = M`是一个语法糖，它等价于`TM = M('TM', (), {})`

### 9.4 元类的作用

元类的作用：控制类的创建过程。

例子: 让定义的类的所有方法和属性名称前面都加上`my_`前缀：

```
class PrefixMetaclass(type):
    def __new__(cls, className, bases, attrs):
        _attrs = dict(('my_' + name, value) for name, value in attrs.items())
        return type.__new__(cls, className, bases, _attrs)
        # return type(className, bases, _attrs)
        # return super(PrefixMetaclass, cls).__new__(cls, className, bases, _attrs)


class Foo(object):
    __metaclass__ = PrefixMetaclass  # 这样Foo就是PrefixMetaclass的实例了
    name = 'foo'

    def bar(self):
        return 'bar'


foo = Foo()
print foo.name    # AttributeError: 'Foo' object has no attribute 'name'
print foo.my_name # foo
print foo.bar()   # AttributeError: 'Foo' object has no attribute 'bar'
print foo.my_bar()# bar

```

参数解释：

- cls：指向当前类PrefixMetaclass
- className: 后面要创建的类名字
- bases: 要创建的类的父类
- attrs: 要创建的类的属性和方法，为一个字典

最后三个return语句本质上是相同的。

### 9.5 应用

例1:创建一个静态类(static class): 不允许创建实例，通常作为工具类(Utility)存在:

```
class StaticMetaclass(type):
    def __new__(cls, name, base, attr):
        ret = type.__new__(cls, name, base, attr)  # 创建类实例

        def ctor(cls, *args, **kwargs):
            raise RuntimeError("Cannot create a instance of the static class!")

        ret.__new__ = staticmethod(ctor)  # 无法实例化

        return ret

class Data(object):
    __metaclass__ = StaticMetaclass

Data()  # RuntimeError: Cannot create a instance of the static class!
```

例2: 创建一个密封类(sealed class)：禁止被继承

```python
class SealedMetaclass(type):
    _types = set()
    
    def __init__(cls, name, base, attr):
        if cls._types & set(base):  # 其实是只能继承自object，创建的类_types非空，再创建子类会报错
            raise SyntaxError("Cannot inherit form a sealed class!")
        cls._types.add(cls)

class A(object):
    __metaclass__ = SealedMetaclass

class B(A):
    pass
# SyntaxError: Cannot inherit form a sealed class!
```
---------
[原载网址：](https://wizyoung.github.io/Python2%E7%AC%94%E8%AE%B0-%E7%B1%BB/)
