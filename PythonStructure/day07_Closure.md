# 闭包Closure

### 回顾 嵌套函数如下：

函数不仅可以定义在模块的最外层，还可以定义在另外一个函数的内部，像这种定义在函数里面的函数称之为嵌套函数（nested function）例如：
```python
def print_outer():
    # print_outer 是外围函数
    message = "it is python of print_outer."

    def inner():
        # inner是嵌套函数
        print(message)
    inner()

print_outer()
```
对于嵌套函数，它可以访问到其外层作用域中声明的非局部（non-local）变量，比如代码示例中的变量 message 可以被嵌套函数 inner 正常访问。

那么有没有一种可能即使脱离了函数本身的作用范围，局部变量还可以被访问得到呢？答案是闭包.

```python
def print_outer():
    # print_outer 是外围函数
    message = "it is python of print_outer."

    def inner():
        # inter是嵌套函数
        print(message)
    return inner

fun1 = print_outer()
fun1()
```
同样输出 "zen of python"。不同的地方在于内部函数 printer 直接作为返回值返回了。

一般情况下，函数中的局部变量仅在函数的执行期间可用，一旦 print_msg() 执行过后，我们会认为 msg变量将不再可用。然而，在这里我们发现 print_msg 执行完之后，在调用 another 的时候 msg 变量的值正常输出了。

### 闭包的作用，闭包使得局部变量在函数外被访问成为可能。

闭包，顾名思义，就是一个封闭的包裹，里面包裹着自由变量，就像在类里面定义的属性值一样，自由变量的可见范围随同包裹，哪里可以访问到这个包裹，哪里就可以访问到这个自由变量。

当函数离开创建环境后，依然持有其上下文状态。 将组成函数的语句和这些语句的执行环境打包在一起时,得到的对象称为闭包。

- 说明:如果一个内嵌函数访问函数外部作用域的变量,则这个函数就是闭包。

### 为什么要使用闭包

闭包避免了使用全局变量，此外，闭包允许将函数与其所操作的某些数据（环境）关连起来。这一点与面向对象编程是非常类似的，在面对象编程中，对象允许我们将某些数据（对象的属性）与一个或者多个方法相关联。

一般来说，当对象中只有一个方法时，这时使用闭包是更好的选择。


示例1:
```python
def adder(x):
    def wrapper(y):
        return x + y
    return wrapper

adder5 = adder(5)
print(adder5)
adder5(10)
print(adder5(10))
print(adder5(6))
print(adder.__closure__)
print(adder5.__closure__)
print(adder5.__closure__[0].cell_contents)

#输出如下：
<function adder.<locals>.wrapper at 0x10378b840>
15
11
None
(<cell at 0x1035bc258: int object at 0x103463d90>,)
5
```
这比用类来实现更优雅，此外**装饰器**也是基于闭包的一中应用场景。

所有函数都有一个 __closure__属性，如果这个函数是一个闭包的话，那么它返回的是一个由 cell 对象 组成的元组对象。cell 对象的cell_contents 属性就是闭包中的自由变量。

```python
print(adder.__closure__)
print(adder5.__closure__)
print(adder5.__closure__[0].cell_contents)
# 输出如下：
None
(<cell at 0x10fc68258: int object at 0x10fb0ed90>,)
5
```

示例:（functional_programming/closure.py）
```python
def make_power(x):
    def fn(arg):
        return arg ** x
    return fn

f2 = make_power(2)  # (make_power(2))(100)
print(f2)
y = f2(100)         # 10000
print(f2(100))
f3 = make_power(3)
print(f3(3))        # 27
f4 = make_power(4)
print(f4(2))        # 16

#输出结果如下：
<function make_power.<locals>.fn at 0x005BD6A8>
10000
27
16
```