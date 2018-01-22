## python 注释
「#」注释是以 # 号开头，直至行尾
作用： 让#号后的字符不参与执行

「#"""和'''」

## 解释器和编译器的区别

python程序的组成<br>
————程序由模块组成<br>
————模块由语句，函数，类等组成<br>
————语句包含表达式　<br>
————表达式建立并处理对象

## 文件后缀
常用的程序文件的后缀:
>  | .c               | ——C语言<br>
>  | .cpp/.cxx/.cc/.C | ——C++语言 <br>
>  | .java            | ——Java语言 <br>
>  | .py              | ——Python语言 <br>
>  | .pyc	      |——Python字节码文件 ( c:code-byte) <br>
>  | .pyo             | ——Python优化文件 (o:optimizing)

## 基本输出函数
- print(python3)    
  简单格式： <br>
  print(值1, 值2, ...)    
  例： 
```python
a = 100
print()  # 输出空行
print(1)
print(1,2,3,4)
print(a)
print("a = ",a)
print("a = %d" % a)
#输出结果如下：
1
1 2 3 4
100
a =  100
a = 100
```

## 交互模式
在python交互模式下编写执行代码 <br>
$ python3 <br>
`>>> `

## 退出交互模式：
- 方法1:
   ` >>> exit()`
- 方法2:
  `ctrl + d`  (快捷键可以退出)

## 在交互模式下查看当前作用域的所有变量——help()函数,> q #退出键
```python
help("__main__")
#输出结果如下：
Help on module __main__:

NAME
    __main__

DATA
    __annotations__ = {}

FILE
    /Users/..../test.py
```
## 输入重定向:
  $ 命令 < 输入文件
  作用:将文件中的内容重定向为一个命令的输出
  注：此时标准键盘输入可能无效