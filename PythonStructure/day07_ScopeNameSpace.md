python作用域和命名空间
- 局部作用域(函数内)  Local                       L
- 外部嵌套函数作用域  Enclosing function locals   E
- 函数定义所在模块(文件)的作用域  Global(module)   G
- Python内置模块的作用域  Built-in(Python)        B

===================================================

# 变量名解析：LEGB原则

- 局部变量：定义在函数内部的变量(包含函数参数)
- 全局变量：定义在函数外部，模块内部的变量

- 变量名的查找规则:

 在访问变量时，先查找本地变量,然后是包裹此函数的外部函数的函数内部的变量，之后是全局变量，最后是内置变量
     L -->  E  --> G --> B

示例：
```python
v = 100  # <<<--- 此为全局变量

def fn():
    v = 200  # <<<--- 此为局部变量
    print(v)

fn()  # 200
print(v)  # 100
```

# python作用域

作用域,是python程序的一块文本区域，是变量或函数访问的时候查找名称的范围空间

### python作用域4个分类:
- 局部作用域(函数内)  Local                       L
- 外部嵌套函数作用域  Enclosing function locals   E
- 函数定义所在模块(文件)的作用域  Global(module)   G
- Python内置模块的作用域  Built-in(Python)        B

示例见：

```python
"""
展示4个作用域 __doc__
"""
v = 100  	# 全局作用域G

def fun1():
    v = 200  			# 外部嵌套函数作用域E
    print("fun1.v =", v)	# fun1.v = 200
    def fun2():
        v = 300  		# 局部作用域L
        print("fun2.v =", v)	# fun2.v = 300
    fun2()

fun1()
print("v =", v)		# v = 100

print(__doc__)		# None
# 模块本身是一个对象，而每个对象都会有一个__doc__属性。该属性用于描述该对象的作用
```
## 全局和局部作用域：

示例：（scope/global_local.py）
```python
v = 100
def fn():
    v = 200
    print(v)    # 200
fn()
print(v)	# 100
```

- 说明
  在默认情况下,不同作用域的同名变量不能直接访问。

在同作用域下，变量的赋值是可以创建或修改变量。

## 全局声明 global

问题：如果想在局部作用域内访问全局变量，怎么办？
​	
### global 语句

- 作用：
  告诉解释器，global语句声明的一个或多个变量，这些变量的作用域为模块级的作用域，也称作全局变量。    
  对全局声明(global)的变量赋值将映身到模块文件的内部作用域。

- 语法:global 变量名1, 变量名2,...

示例: （scope/global_declare.py）
```python
v = 100

def fn():
    global v	#声明全局变量v
    v = 200  # 修改全局的v变量

fn()
print(v)     # 200
```
示例：（19_global_param_list.py）
```python
v = 100

def fn(v):
	global v	# v出现在了参数列表里，SyntaxError: name 'v' is parameter and global
	print(v)

fn(200)
```

- global说明:
1. 全局变量如果要在函数内部被赋值,则必须经过全局声明,否则被认为是局部变量
2. 全局变量在函数内部不经过声明就可以直接读取访问(前题是变量已经存在)
3. 不能先声明局部变量,再用global声明为全局变量,此做法不附合语法规则
4. global变量列表里的变量名不能出现在此作用域的参数列表里,for循环控制目标,类定义,函数定义及import导入名字中

## 函数嵌套

函数嵌套是指一个函数里用def语句来创建其它函数的情况

嵌套示例：（scope/fn_embeded.py）
```python
def fn_outer():  # 外部函数
    print("外部函数被调用")
    def fn_inner():
        print("fn_inner被调用")
    fn_inner()
    fn_inner()
    print("外部函数调用结束")
fn_outer()
# fn_inner() 　# 错的，内嵌函数只存在于函数内部
# 输出结果如下：
外部函数被调用
fn_inner被调用
fn_inner被调用
外部函数调用结束
```
### nonlocal语句

nonlocal语句与global语句类似，只不过它用来声明嵌套作用域，而不是全局作用域。nonlocal语句允许对嵌套的函数作用域中的名称赋值，并且把这样的名称的作用域查找限制在嵌套的def中

- 作用:告诉解释器,nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量

- 语法:
  nonlocal 变量名1, 变量名2,...

示例:（scope/nonlocal.py）
```python
g_var = 100

def outter():
	e_var = 200
	def inner():
	    nonlocal var  # 指定var为外层嵌套函数作用域
#	    global var
	    var += 1  # 此行会出错
	    print("inner.var=", var)
	inner()
	print("outter.var=", var)

outter()

```
示例：（scope/nonlocal2.py）
```python
var=100
def f1():
    v = 200
    def f2():
        v = 300
        def f3():
            nonlocal v
            v = 400
            print('f3.v=',v)
        f3()
        print('f2.v=', v)
    f2()
    print('f1.v=', v)
f1()
print
#输出结果如下：
f3.v= 400
f2.v= 400
f1.v= 200
```

说明:
    1. nonlocal语句只能在被嵌套函数的内部进行使用
    2. 访问nonlocal变量将对外部嵌套函数的作用域内的变量进行操作
    3. 当有两层或两层以上函数嵌套时,访问nonlocal变量只对最近一层的变量进行操作
    4. nonlocal语句的变量列表里的变量名,不能出现在此作用域的参数列表中

- globals() / locals()函数
  globals() 返回当前全局作用域内变量的字典
  locals()  返回当前局部作用域内变量的字典

示例:
```python
a = 1
b = 2
def fn(c, d):
   e = 300
   print("locals 返回:", locals())  # {'e': 300, 'c': 100, 'd': 200}
   print("globals返回:", globals()) # {'a': 1, 'b': 2, 'fn': <xxxxxx>}

fn(100, 200)
#输出结果如下：
locals 返回: {'e': 300, 'd': 200, 'c': 100}
globals返回: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x002C84D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:/newPY/newpro/textLC.py', '__cached__': None, 'a': 1, 'b': 2, 'fn': <function fn at 0x021B1A50>}

```