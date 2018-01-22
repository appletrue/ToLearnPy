- 布尔运算：not/and／or

- 逻辑位运算：位与／位或／位异或／左移／右移／位求反

- 成员运算符：in ／not in

  运算符优先级

  ​
## 布尔运算:

— 运算符: not  and  or
——解释：
- 1&2 ：位逻辑与
- 1&&2：逻辑与  ==》and

### not 运算符

- 作用：逻辑取反
- 语法:  not 表达式
- 例:
```python
print(not True)
print(not False)  # True
print(not 100)  # False  相当于 not bool(100)
print(not 0.0)  # True
print(not 0J)  # True
print(not 1 + 2J) # False
print(not '')  # True
print(not "False")  # False
print(not None)  # True
print(None == 0) #False
#输出结果如下：
False
True
False
True
True
False
True
False
True
False
```
"False"(字符串) 和 False(布尔类型)

### and 运算符:

- 作用：返回优先为假值(False)的对象

- 语法：表达式1 and 表达式2
  例：
```python
print(0 and 100)  # 返回0
print(100 and 200)  # 返回200
print(100 and 0)  # 返回0
```
- 说明：
  当表达式1的布尔测试值为True时，返回 表达式2，否则返回表达式１　

| bool(表达式1) | bool(表达式2) | 布尔测试值 |
| ---------- | ---------- | ----- |
| False      | False      | False |
| False      | True       | False |
| True       | False      | False |
| True       | True       | True  |

- and 真值表:

x and y<br>
bool(x)    返回值<br>
True        y<br>
False       x

### or 运算符:

作用：优先返回值为真(True)的对象<br>
语法：表达式1 or 表达式2<br>
例：
```python
print(0 and 100)  # 返回100
print(100 and 200)  # 返回200
print(0.0 and 0)  # 返回0.0
print(3.14 or 0.618) #返回3.14
```

- 正负号运算符：+(正号)  -(负号)
  语法: 一元运算符
  - `+`表达式 
  - `-`表达式

## 位运算:

- 运算符:
  -  &  位与
  -  |  位或
  -  ^  位异或
  -  << 左移
  -  `>>`右移
  -  ~  求反

--bitmap 位图 cache

### & 位与: 

语法 :  表达式x & 表达式y<br>
作用：按位操作,两个对应的位都为1,则结果为1；两个对应的位只要有一个为0，则结果为0。

示例：<br>
```python
x = 10
y = 20
print(x & y) #输出 0 
print(bin(x))  # 0b1010
print(bin(y))  #0b10100
#详解：
10 & 20 = 0b01010
       &  0b10100
            00000
```

- bin(x)函数:  bin(x)  将x转换为二进制(binary)的字符串

### | 位或：

语法:  表达式x | 表达式y<br>
作用：<br>
  ——按位操作,两个对应的位只要有一个为1,则结果为1<br>
  ——两个对应的位都为0，则结果为0<br>
示例：
```python
x = 10
y = 20
print(x | y) 
#详解：
10 | 20 = 0b01010
          0b10100
            11110 = 16+ 8+4+2 = 30
```
### ^ 位异或 (半加运算)

语法:表达式x ^ 表达式y<br>
作用：按位操作,两个对应的位不同，结果为1；两个对应的位相同，结果为0<br>

```python
x+y = 0+0 = 0
    = 1+1 = 0
    = 1+0 = 1
    = 0+1 = 1
```

### << 左移运算

语法格式：表达式x << 整数表达式y<br>
作用：将x的二进制值，按位向左移动y位，低位补0<br>
例：x = 6 << 1

### >>右移运算

语法格式：表达式x >> 整数表达式y<br>
作用：将x的二进制值,按位向右移动y位，低位溢出丢弃<br>

例:

```python
   6 >> 1   #3
   6 >> 2   # 1
   6 >> 3   # 0
   6 >> 100 # 0
```

### ~ 按位求反

语法格式:  ~ 表达式<br>
作用：将数据二进制相应位取反<br>

例:  ~ 6

计算优化：
```python
a=6
b=12
c=a*b
c=a<<3+a<<2
c=a*(8+4)
= a*8 + a*4
= a<<3 + a<<2
d=100
e=8
f = d%e = 100%8 = 4
```

## in & not in 成员运算符

作用：<br>
 —— in 用于序列，字典，集合中，用于判断某个值是否存在于对象中<br>
 —— not in 的返回值与in相反<br>
例：

```python
x = "welcome to tarena!"
if 'to' in x:
    print("'to' 在 x 字符串中")
```
## python 运算符的优先级:

| 运算符                      | 描述                    |
| ------------------------ | --------------------- |
| **                       | 指数(最高优先级)             |
| ~ + -                    | 位反转，一元加号(正号),一元减号(负号) |
| `*`/ // %                | 乘，除，地板除，求余            |
| `+ - `                   | 加，减                   |
| << >>                    | 左移，右移                 |
| &                        |                       |
| ^                        | 位异或                   |
| < <= > >=                | 小于，小于等于,大于，大于等于       |
| == !=                    | 等于,不等于                |
| = %= /= //= -= += *= **= | 复合赋值运算符               |
| is, is not               | 身份运算符                 |
| in, not in               | 成员运算符                 |
| not, or, and             | 逻辑运算符                 |