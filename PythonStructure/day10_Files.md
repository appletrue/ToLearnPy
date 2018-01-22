@@ -1,208 +0,0 @@

# 文件

- 什么是文件

文件是用于数据存储的单位,通常用于长期存储数据。Linux/Unix下文件可分为普通文件和设备文件，普通文件是由文件名和文件中的数据两部分组成的

### 文件的打开和关闭

  文件需要在使用时先打开才能读写
  在不需要读写文件时,应及时关闭文件以释放系统资源
  任何操作系统,打开的文件数有最大限制

- 打开文件的函数:

```
open(file , mode='r')用于打开一个文件,返回此文件的操作对象,如果打开失败则会触发错误,抛出异常 
```

- 文件关闭的方法:

F.close()    #  关闭文件,释放系统资源

### 文本文件的常用方法:

- F.readline() 读取一行数据,如果到达文件尾则返回空行
- F.readlines([n]) 返回每行字符串的列表, n代表最大字符数(字节数)
- F.writelines(lines) 写入字符中的列表
- F.flush()   把写入文件对象的缓存内容写入到磁盘
- F.write(x)  将数据(字符/字节)写入到文件中

### 模式字符串的含义:

```python
  'r' 以只读方式打开文件(默认)

  'w' 以只写方式打开文件,删除原有文件内容(如果文件不存在,则创建该文件并以只写方式打开文件)

  'x' 创建 一个新文件,并以写模式打开文件,如果文件存在则会产生FileExistsError错误

  'a' 以追加写方式打开一个文件,如果有原文件则追加到原文件末尾

  'b'  用二进制模式打开

  't'  用文本文件模式打开(默认)

  '+'  为更新内容打开一个磁盘文件(可读可写)

注:缺省模式是'rt'

  'w+b' 可以实现二进制的随机读写.

  'r+b' 以二进制只读形式打开文件,打开文件时不会清空文件内容

  'r+' 以文本模式打开文件,打开文件时不清空文件内空,可以对文件进行写操作

```

## 二进制文件

bytes 类型 和 bytearray类型 
汉字编码

### bytes类型

  以字节为单位存储数据,每个字节的值为0-255  [0~2**8-1]

#### bytes常量的表示方式:

  b''      空字节串
  b'ABCD'  有四个字节的字节串
  b'\x41\x42' 有两个字节的字节串

#### bytes运算:

- += * *=
  < <= > >= == != 
    in / not in 

```
B = b'ABCDEFG'
b'D' in B   # True
```

#### bytes 相关的函数:

  len(x)  求字节个数
  max(x)
  min(x)
  sum(x)
  any(x)
  all(x)

#### 创建字节串(bytes)的函数

bytes()   创建空的字节串
bytes(整数)  
bytes(整型可迭代对象)
bytes(字符串, encoding='utf-8')

字节串可以看做是序列
字节串是不可变的

> > > help(bytes) 查看帮助

### bytes和str转换

- str ---> bytes

```
str.encode(encoding='utf-8') 方法来转换
```

例:

```
b = "英文abc".encode('utf-8')
```

- bytes ---> str

  B.decode(encoding='utf-8')
  例:
  s=b'\xe8\x8b\xb1\xe6\x96\x87abc'.decode('utf-8')

### 二进制文件的读写

#### 什么是二进制文件:

  文件中以字节(byte)为单位存储,不以换行符(\n)为单位分隔内容的文件

#### 二进制文件操作的方法:

-   F.read(size=-1)  从一个文件流中最多读陂size个字符
-   F.write(字符串/字节串)  写一些数据到文件流中,返回写入的字节数(字符数)
-   F.tell()  返回当前文件流的绝对位置
-   F.seek(cookie, whence=0) 改变数据流的位置,返回新的绝对位置
-   F.readable()  判断这个文件是否可读,可读返回True
-   F.writable()  判断这个文件是否可写,可写返回True

#### F.read() 返回类型:

 文本文件, 返回字符串
 二进制文件,返回字节串(字节序列)

#### F.write(x) 函数

#### F.seek(偏移量, whence=相对位置)

  偏移量:

```
大于0的数代表向文件尾方向移动
小于0代表向文件头方向
```

  相对位置:

```
0 代表从文件头开始偏移
1 代表从前位置开始偏移
2 代表从文件尾开始偏移
```

### bytearray 类型

bytes类型为不可变类型 
bytearray类型为可变的数据类型

操作:

`- + = * *= `
比较运算: < <= > >= == != 
  in / not in 运算符
  index /slice 

#### bytearray 的方法:

- B.clear()  清空
- B.append(n)  追加一个字节(n为0-255的整数)
- B.remove(value) 删除第一次出现的字节,如果没有出现,则产生ValueError错误
- B.reverse()   字节的顺序进行反转
- B.decode(encoding='utf-8')
- B.find(sub[, start[, end]])

#### 创建bytearray的函数

-   bytearray()   创建空的字节串
-   bytearray(整数)  
-   bytearray(整型可迭代对象)
-   bytearray(字符串, encoding='utf-8')

练习:有一个bytearray字节序列:
   ba=bytearray(b'a1b2c3d4')
   如何得到字符串 '1234'和'abcd'

   将上述bytearray改为bytearray(b'A1B2C3D4')

### 标准输入输出文件:

  sys.stdin
  sys.stdout
  sys.stderr

#### 模块 sys

Linux 下 Ctrl + D 输入文件结束符
输入重定向的文件内容将发送给sys.stdin