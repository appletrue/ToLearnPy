# 装饰器 decorator　

装饰器是一个函数,主要作用是用来包装另一个函数或类，包装的目的是在不改变原函数名的情况下，改变被包装函数(对象)的行为

### 装饰器函数
```python
def 装饰器函数名(参数):
     函数块
    return 函数
```
示例：(deco.py)
```python
def deco(fn):
    print("装饰器函数被调用，并返回原函数")
    return fn
@deco
def myfunc():
    print("函数myfunc被调用!")

# 以上@deco等同于此语句
# myfunc = deco(myfunc)

#执行
myfunc()

# 输出结果如下：

装饰器函数被调用，并返回原函数　
函数myfunc被调用!
```

被装饰函数带有参数的装饰器

示例：（deco2.py）
```python
def msg_service(fn):
    def savemoney2(name, x):
        print("welcome", name, "to HSBC,please get ur number!!!")
        fn(name, x)
        print(name, "deposited $", x, "to ur account,the message is being sending...")
    return savemoney2

@msg_service
def savemoney(name, x):
    print(name, "deposit", x, "dollars")

savemoney("sam", 200)
savemoney("rose", 500)

#输出结果如下：
welcome sam to HSBC,please get ur number!!!
sam deposit 200 dollars
sam deposited $ 200 to ur account,the message is being sending...
welcome rose to HSBC,please get ur number!!!
rose deposit 500 dollars
rose deposited $ 500 to ur account,the message is being sending...
```

被装饰函数带有不定参数的装饰器

示例：（deco3.py）
```python
def deco(func):
	def _deco(*args, **kwargs):
		print("before %s called." % func.__name__)
		ret = func(*args, **kwargs)
		print("  after %s called. result: %s" % (func.__name__, ret))
		return ret
	return _deco

@deco
def myfunc(a, b):
	print(" myfunc(%s,%s) called." % (a, b))
	return a+b

@deco
def myfunc2(a, b, c):
	print(" myfunc2(%s,%s,%s) called." % (a, b, c))
	return a+b+c

myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)
```
# 带参数的装饰器函数语法:

@ 装饰器函数名[(装饰器函数传参)]<换行>
def 函数名(参数列表):
    语句块

示例：()
```python
def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("mymodule")
def myfunc():
    print(" myfunc() called.")

@deco("module2")
def myfunc2():
    print(" myfunc2() called.")

myfunc()
myfunc2()
```