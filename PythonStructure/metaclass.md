# Python中的元类

------
1. 继承与实例化
2. type的用法
3. 元类metaclass
4. 元类的作用
5. 应用
-------

## 1. 继承与实例化

在面向对象体系里面，存在两种关系：

- 继承关系：在python里面用`__base__`可查看，顶层是`object`
- 实例关系：表现为某个类型的实例化。在python里面用`__class__`查看，顶层为`type`。

```python
print(object.__base__)  # 继承关系上object为顶层
None
print(object.__class__)  # object是type的实例
<type 'type'>

print(type.__base__)  # type继承自obect
<type 'object'>
print(type.__class__)  # type是type的实例
<type 'type'>

# python中type和object就像鸡和蛋的关系
print(int.__base__)  # int继承自object
<type 'object'>
print(int.__class__)  # int是type的实例
<type 'type'>
```

一个实例化的例子：

```python
print(class A(object):
... 	pass 
a = A()
print(a.__class__)  # a是A的实例
<class '__main__.A'>
print(a.__base__)  # 报错。实例没有继承关系，所以没有__base__属性
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__base__'
```

## 2. type的用法

- `type(obj)`：获取对象的相应类型，与`obj.__class__`等同
- `type(className, (parents), {attr: value})`：创建并返回一个类，三个参数分别对应与类名(字符串)，父类(元组形式)，属性(字典形式)

因此以下两个语句等价：

```python
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

## 3. 元类metaclass

先总结下：

- 类的类就是元类(强调实例化)，默认是type


- type是所有元类的**Father**
- 在实例化时，也就是创建类型对象时，会按以下顺序查找`__metaclass__`属性：

`class.__metaclass__ -> bases.__metaclass__ -> module.__metaclass__ -> type`

理解以上几点，看下面例子：

```python
class M(type):
... 	pass
print(M.__class__)
<type 'type'>
print(M.__base__)  # 继承自type
<type 'type'>
```

上面的M就是一个元类。要实例化，可定义一个类：

```python
class TM(object):
 	__metaclass__ = M  # 指定元类
print(TM.__class__)
<class '__main__.M'>
print(TM.__base__)
<type 'object'>
```

其实上面的`__metaclass__ = M`是一个语法糖，它等价于`TM = M('TM', (), {})`

## 4. 元类的作用

元类的作用：**控制类的创建过程**。

例子: 让定义的类的所有方法和属性名称前面都加上`my_`前缀：

```python
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
print(foo.name)    # AttributeError: 'Foo' object has no attribute 'name'
print(foo.my_name) # foo
print(foo.bar())   # AttributeError: 'Foo' object has no attribute 'bar'
print(foo.my_bar())# bar
```

参数解释：

- cls：指向当前类PrefixMetaclass
- className: 后面要创建的类名字
- bases: 要创建的类的父类
- attrs: 要创建的类的属性和方法，为一个字典

最后三个return语句本质上是相同的。

## 5. 示例

例1:创建一个静态类(static class): 不允许创建实例，通常作为工具类(Utility)存在:

```python
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

------

参考资料：

[Pyton之旅](http://funhacks.net/)

[使用元类 - 廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820064557c69858840b4c48d2b8411bc2ea9099ba000)

[Python:元类metaclass](http://gohom.win/2015/10/23/pyMetaClass/)

[Python Types and Objects](http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html)
