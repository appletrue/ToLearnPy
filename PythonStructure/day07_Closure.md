# 闭包Closure

### 回顾 嵌套函数如下：

函数不仅可以定义在模块的最外层，还可以定义在另外一个函数的内部，像这种定义在函数里面的函数称之为嵌套函数（nested function）例如：
```python
def print_outer():
    # print_outer 是外围函数
    message = "print_outer."

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
    message = "Outer print."

    def inner():
        # inter是嵌套函数
        print(message)
    return inner

fun = print_outer()
fun()
```
同样输出 "Outer print.",不同的地方在于内部函数 inner 直接作为返回值返回了。

一般情况下，函数中的局部变量仅在函数的执行期间可用，一旦 print_outer() 执行过后，我们会认为 message变量将不再可用。然而，在这里我们发现 print_outer 执行完之后，在调用 fun() 的时候 message 变量的值正常输出了。

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

f = adder(5)
print(f)                        #<function adder.<locals>.wrapper at 0x03DEF660>
print(f(10))            #15
print(f(6))             #11


```
这比用类来实现更优雅，此外**装饰器**也是基于闭包的一中应用场景。

所有函数都有一个 __closure__属性，如果这个函数是一个闭包的话，那么它返回的是一个由 cell 对象 组成的元组对象。cell 对象的cell_contents 属性就是闭包中的自由变量。

```python
print(adder.__closure__)        # None
print(f.__closure__)            # (<cell at 0x007352B0: int object at 0x61B968C0>,)
print(f.__closure__[0].cell_contents)      # 5

```
这解释了为什么局部变量脱离函数之后，还可以在函数之外被访问的原因的，因为它存储在了闭包的 cell_contents中了

示例:（functional_programming/closure.py）
```python
def make_power(x):
    def fn(arg):
        return arg ** x
    return fn

f2 = make_power(2)      # (make_power(2))(100)
print(f2)
y = f2(100)             # 10000
print(f2(100))
f3 = make_power(3)
print(f3(3))            # 27
f4 = make_power(4)
print(f4(2))            # 16

#输出结果如下：
<function make_power.<locals>.fn at 0x005BD6A8>
10000
27
16
```
示例:
```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1.__closure__[0].cell_contents)
print(f1(),f2(),f3())
#输出结果如下：
**3**
9  9  9
```
上一例子中,i并没有在函数中定义，所以f 和外部i 构成闭包，i在range最后取值为3，因此在return fs 这一行的时候，这个闭包里i 的值确定了，每一次调用的结果都是9. **迭代没有作用域的概念，需要手动把它放进闭包里**
对比以下代码中形式，i每个阶段的值，通过默认参数传入j，这时候相当于j拿下了这个接力棒，把中间值都保存下来了，这时候每一个f的构成，没有任何闭包，return之后i就销毁了.
```python
def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
             return j*j
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
print(f1.__closure__[0].cell_contents)   #没有闭包，因为外部遍历i已经传值给默认参数j了
#输出结果如下:
1 4 9
Traceback (most recent call last):
  File "D:/newpro/test.py", line 17, in <module>
    print(f1.__closure__[0].cell_contents)
TypeError: 'NoneType' object is not subscriptable
```
如果不用闭包来定义：可以用匿名函数lambda
```python
f1, f2, f3 =  [lambda :i*i for i in range(1,4)]
print(i)
print(f1(), f2() ,f3())
i = 5
print(f1(), f2() ,f3())
#输出结果:      #这里所有的匿名函数，都会直接读取全局变量i，因此全局变量i的值，结果也会跟着变。
9 9 9
9 9 9
```

不能得到想要的结果,解决办法有以下:
```python
f1, f2, f3 =  [lambda j=i:j*j for i in range(1,4)]

print(f1(), f2() ,f3())
i = 5
print(f1(), f2() ,f3())
print(f1.__closure__)  
#输出结果:
1 4 9
1 4 9
None
```
另一种方式,闭包
```python
def get_fx(number):
    return lambda: number * number

f1, f2, f3 = [get_fx(i) for i in range(1, 4)]
print(f1(), f2() ,f3())
print(f1.__closure__)
#输出结果:
1 4 9
(<cell at 0x006C5350: int object at 0x62FA6880>,)
```

【思考】：  
1，将闭包函数当成一个变量对象来理解，变量都是引用的内存的一个对象;

2，当函数存在嵌套，并且子函数引用了父函数中的变量，可以访问这些变量的作用域就形成闭包。**BUT**如果子函数没有访问父函数中的变量，就不存在闭包。

3,闭包简单来说就是 函数+上下文环境。它能捕获函数外部的变量，持有变量所在环境的一个引用，或者说指针。

4,当程序进入循环，按道理说应该是返回1,4,9这样一个东西,但是，我们返回的是函数，且这个函数在返回时并没有执行，这就意味着i变量指向内存里的那个对象已经为3了,再次PRINT的时候，函数才执行得出结果，计算过程里i都为3，所以结果为9,9,9

5,发现每个函数对象中的func_closure其实是对同一个对象的引用，指向同一块内存。

6,每个函数对象中的func_closure中的cell_contents都为3，而且注意到每个int object的地址也一样，即每个3其实是同一个对象的值。

7,函数对象中的这个func_closure，其本身也是一个对象，其为f1、f2、f3三个对象所引用的同一个包含上下文信息的对象，这里上下文信息内容就是引用了同一个int object

8,闭包仅仅是一个为了保存上下文信息以便在函数调用时正确寻址和取值的存在。

----------
[参考来源网址:](https://foofish.net/python-closure.html)    
[深入理解闭包的解答:](https://stackoverflow.com/questions/36636/what-is-a-closure)    
[知乎关于闭包的解答](https://www.zhihu.com/question/31792789/answer/54189871)    
[深入浅出python闭包](https://zhuanlan.zhihu.com/p/22229197)
