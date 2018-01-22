# 异常

### assert 语句(断言语句)

- 语法:
  assert 真值表达式, 错误数据(通常是字符串)
- 作用:
  当真值表达式为False时,用错误数据创建一个 AssertionError类型的错误,抛出后进入异常状态.    
  等同于:
  if 真值表达式 == False:
      raise AssertionError(错误数据)

示例见:get_score.py
```python
def get_score():
    s = int(input("请输入学生成绩: "))
    assert s <= 100, "错误!,成绩不会大于100分"
    #相当于：
    # if s > 100:
    #     raise AssertionError("错误!,成绩不会大于100分")
    assert s>0,"错误！成绩不会是负分"
    return s

try:
    score = get_score()
    print("学生成绩为:", score)
except AssertionError as err:
    print(err)

print("程序退出")
```

### with 语句
- 语法:
```python
  with 表达式 [as 变量名]:
     语句块
  或
  with 表达式1 [as 变量名1][,表达式2 [as 变量名2]...]:
     语句块
```

- 说明: as 子句中的变量绑定生成的对象

- 作用:使用于对资源进行访问的场合,确保使用过程中不管是否发生异常,都会执行必须的"清理"操作,并释放资源

示例见: with.py
```python
#正常打开文件
f = open("myfile.txt", "r")
while True:
    text = int(input("请输入一个数:"))
    l = f.readline()
    print(l, end='')
    if len(l) == 0:
        f.close()
        print("文件已关闭")
        break


f = open("myfile.txt", "r")
try:
    while True:
        text = int(input("请输入一个数:"))
        l = f.readline()
        print(l, end='')
        if len(l) == 0:
            break
except:
    print('发生异常')
finally:
    f.close()
    print("文件已关闭")

with open("myfile.txt") as f:
    while True:
        # 3 / 0  # 触发异常, 但文件肯定会被关闭
        l = f.readline()
        print(l, end='')
        if len(l) == 0:
            break
```

## 环境管理器:

1.类内有__enter__ 和 __exit__方法的类被称为环境管理器
2.能够用with语句进行管理的对象必须是环境管理器
3.__enter__ 将在进入with语句时被调用并返回 由as 变量管理对象
4.__exit__ 将在离开with时被调用,且可以用参数来判断在离开with语句时是否有异常发生,并做出相应的处理

示例见: cooker.py
```python
class Cooker:  # 厨师
    def open_gas(self):
        print("正在打开天燃气.")
    def close_gas(self):
        print("正在关闭天燃气")
    def doworks(self):
        print("正在制作小甜饼")
    def __enter__(self):
        self.open_gas()
        return self  # 此对象将被 as 绑定
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close_gas()
        if exc_type is None:
            print("with语句正常退出")
        else:
            print("with语句异常退出,", exc_value)


with Cooker() as c:
    c.doworks()  # 工作中...
    3 / 0  # ZeroDivsionError --> 错误对象
    c.doworks() 

# 正常处理流程
# c = Cooker()
# c.open_gas()
# c.doworks()  # 工作中...
# 3 / 0
# c.doworks() 
# c.close_gas()   
```


## Python调试器 pdb模块

pdb 是个模块,主要用于调试程序

作用：
 　1. 让程序单步执行，并跟踪程序的执行流程
  　2. 在运行查看变量的值
  　3. 让程序控制程序的执行流程

方法:
|pdb.set_trace() | 在此代码段进入调试器|


|pdb |调试命令:|
|q/quit    |  退出pdb调试器|
|l/list     | 列出源码|
|h/help      |查看pdb帮助|
|p/pp 表达式  |运行表达式并返回结果|
|n/next      |执行下一条语句|
|c/cont/continue  |继续执行,直到下一个断点|
|b/break |断点位置  设置断点|
|cl/clear  |断点号  清除断点|
|s/step    |进入到函数内部执行|
|r/return  |持续运行,直到此函数返回|
|w/where   |打印函数调用栈|

pdb断点的设置方法:

1) 文件名 : 行号
   (Pdb)  b test_pdb.py : 19
2) 当前文件的行号
   (Pdb) b 20  # 等同于 btest_pdb.py : 20
3) 函数名
   (Pdb) b f1
4) 模块.函数名
   (Pdb) b contra.play


控制台下的pdb调试:
控制台下运行pdb调试器的命令格式:
$ python3 -m pdb xxxx.py
(Pdb) 
注:xxxx.py内不需要导入pdb模块和调用set_trace

```python
pdb.set_trace()
print("这是第1行输出")
print("这是第2行输出")
def f1(n):
	print("这是f1中n的值:", n)
n += 1
print("这是f1中修改后的n的值:", n)
print("这是第3行输出")
调用f1
1(1)
x = 100
y = 200
z = x + y
f1(x)
def f2():
print("f2开始")
f1(10)
print("f2结束")
f2()
print("程序结束:", x, y, z)

```

