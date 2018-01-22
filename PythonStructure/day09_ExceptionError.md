# 异常抛错 (基础)

- 什么是错误

  错误是指由于逻辑或语法错误等,导致一个程序已无法正常执行的问题。

- 什么是异常 

异常是程序出错时标识的一种状态.当异常发生时,程序不会再向下执行,而转去调用此函数的地方,待处理相应的错误并恢复为正常状态。

try 语句(此语句有两种写法)

### try/except/else/finally语句

语法:

```python
try:
    	可能触发异常的语句
except 错误类型1 [as 变量1]:

    	异常处理语句1
except 错误类型2 [as 变量2]
    	异常处理语句2
except (错误类型3, 错误类型4, ...) [as 变量3]
    	异常处理语句3
	    ...
except:
    	异常处理语句other
else:
    	末发生异常语句
finally:
   	 最终语句
```

语法说明:

- except子句可以有一个或多个,但至少要有一个
- as 子句是用于绑定错误对象的变量,可以省略
- else子句最多只能有一个,也可以省略
- finally子句最多只能有一个,也可以省略不写

处理说明:

1. except子句用来捕获和处理当某种类型的错误发生时,处理异常
2. except 子句会根据错误的类型进行匹配,如匹配成功则调用异常处理语句进行处理,然后程序转为正常状态
3. 如果except子句没有匹配到任何类型的异常则转到except:子句
4. 如果没有任何except子句进行处理,则程序的异常状态会继续下去,并向上层传递
5. 如果没有异常,则执行else 子句中的语句
6. 最后执行finally子句中的语句



练习:

写一个程序,输入学生成绩(0~100之间的整数),如果输入出现异常,则设置此成绩变量的值为0



# Python中的错误类型 

| 抛错类型               | 说明                  |
| ------------------ | ------------------- |
| ZeroDivisionError  | 除(或取模)零             |
| StopIteration      | 迭代器没有更多的值           |
| OverflowError      | 数值运算超出最大限制          |
| IOError            | 输入/输出操作失败           |
| ImportError        | 导入模块错误              |
| GeneratorExit      | 生成器发生异常来通知退出        |
| IndexError         | 序列中没有此索引            |
| FloatingPointError | 浮点计算错误              |
| IndentationError   | 缩进错误                |
| TypeError          | 对类型无效的操作            |
| ValueError         | 传入无效的参数             |
| AssertonError      | 断言语句失败              |
| NameError          | 未声明/初始化对象           |
| AttributeError     | 对象没有这个属性            |
| KeyboardInterrupt  | 用户中断执行(通常是输入Ctrl+c) |

更多见: >>> help(builtins)

### try/finally 语句

- 语法:
```Python3
    try:
        可能触发异常的语句
    finally:
        最终语句
```
- 说明:

1. finally子句不可以省略
2. 一定不存在except 子句

- 作用:

  通常用try/finally语句来做触发异常时必须要处理的事情,无论异常是否发生,finally子句都会被执行

注: try/finally语句不会改变程序的(正常/异常)状态

示例见:try_finally.py

try嵌套 :

示例:
```Python3
try:
    try:
        d = int(input("输入一个数:"))
        a = 3 / d
    finally:
        print("内部finally已执行")
except:
    print("有异常发生")
finally:
    print("外部finally已执行")
```
### raise 语句

- 作用:生成一个错误,让程序进入异常状态

- 语法:raise 异常类型 或 raise 异常对象

示例见: raise.py