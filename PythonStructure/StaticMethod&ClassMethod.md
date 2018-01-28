# Python中的类方法和静态方法

对一个类，我们要调用它的一个方法，必须要绑定实例，而不能直接通过`类名.方法名()`的形式调用。因此，想要通过类来调用方法，而不是通过实例，可以使用**静态方法**`@staticmethod`和**类方法**`@classmethod`的形式实现。

二者的形式：

- @classmethod修饰的方法的第一个参数必须是cls。cls指的是类的本身，若有继承出现，cls指当前类。
- @staticmethod修饰的方法没有self和cls参数，可以不接受参数


考虑如下的Date类：

```python
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

```Python
day, month, year = map(int, string_data.split('-'))
data1 = Data(day, month, year)
```

这样将代码放在类外单独处理，固然可以，但是若能让类本身就能处理这种非标准输入不是更好吗？后者显然维护起来更方便。

用类方法实现如下：

在Date中加入这样一个类方法：

```python
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

```python
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

```python
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

```python
new_year = Date(1, 1, 2013)                # Creates a new Date object
millenium_new_year = Date.millenium(1, 1)  # also creates a Date object. 

# Proof:
print(new_year.display())            # "1-1-2013"
print(millenium_new_year.display())  # "1-1-2000"

print(isinstance(new_year, Date))  # True
print(isinstance(millenium_new_year, Date))  # True
```

这时来了一个Date类的子类DateTime:

```python
class DateTime(Date):
  def display(self):
      return "{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year)
```

使用：

```python
datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)

print(isinstance(datetime1, DateTime))  # True
print(isinstance(datetime2, DateTime))  # False

print(datetime1.display())  # returns "10-10-1990 - 00:00:00PM"
print(datetime2.display())  # returns "10-10-2000"
```

显然`datetime2`是`Date`的实例而不是`DateTime`的实例。

很多情况下，我们并不希望是这样的结果，我们希望上面的`datetime2`按所在子类指定的形式显示。怎么做呢？使用类方法。将Date类的静态方法替换为下面的类方法：

```python
@classmethod
def millenium(cls, month, day):
    return cls(month, day, 2000)
```

这时候再使用：

```python
datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)  # 这里cls会指向DateTime

print(isinstance(datetime1, DateTime))  # True
print(isinstance(datetime2, DateTime))  # True

print(datetime1.display())  # "10-10-1990 - 00:00:00PM"
print(datetime2.display())  # "10-10-2000 - 00:00:00PM"
```

总结：

- 静态方法其实就是一个定义在类中的方法，只是调用时可以不需要先对类进行实例化，直接用类调用即可。无论后面怎么继承，它的实现不变。
- 类方法也在调用时也不需要先对类进行实例化，但是它的实现，在继承时是跟随当前的子类的(因为它的第一个参数永远是cls)
- 它们常用于将数据预处理等封装在类内，避免代码扩散到类外不好维护。

------

参考资料：

[stackoverflow–Python @classmethod and @staticmethod for beginner?](http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner)

[知乎–Python 中的 classmethod 和 staticmethod 有什么具体用途？](https://www.zhihu.com/question/20021164)
