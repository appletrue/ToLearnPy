# 一些小练习:
1. 5位数，把每个位求出(取余）12345……1,2,3,4,5
2. 改写圆的周长和面积的计算用变量代替某些值
3. 从凌晨00:00:00　计时，到现在已经过了63320秒，请问，现在是几时,几分，几秒,写程序打印出来
4. 在终端输出图形:
   *
  ***
 *****
*******

5. if语句嵌套练习,季节嵌套:
  输入1~12个月,超出此范围提示不合法:
  1-3 春季
  4-6 夏季
  ....
  要求：输入月份打印季节(用if语句嵌套实现)

6. 北京出租车计价器:
  收费标准:3公里以内收费13元,基本单价 2.3元公里(超出3公里以外);空驶费: 超过15公里后，每公里加收单价的50%(部分算法)
  要求：输入公里数，打印出费用金额
  
7.输入语文，数学，英文的三科成绩,打印出最高是多少，最低分是多少,平均分是多少

8.分三次输入当前的小时，分钟和秒数,打印此时距离0:0:0已过了多少秒

9.输入一个季度1~4的数字，输出这个季度有哪几个月份。

10.指定一个圆的半径是3cm,计算圆的周长是多少?计算圆的面积是多少?
  要求使用Python交互模式进行计算
结果：
周长:18.84955592153876
面积:28.274333882308138
              
11. IP = 0xc0a80164       # IP: 192.168.1.100<br>
  MASK = 0xFFFFFF00     # 子网俺码 255.255.255.0<br>
  求：IP & MASK   的值   # 网段地址:192.168.1.0<br>
  求: IP | ~MASK  的值   # 广播地址:192.168.1.255<br>
  					0.0.0.255<br>
hex(x) 将一个整数转为16进制的字符串<br>
255 ->0b11111111

12. 任意输入一个字符串,计算要输入的字符'a'的个数，并打印出来
例如:  请输入: abcdabcabazzzzzz  打印 4

13. 用字符串 * 运算符打印三角形
要求输入一个整数，此整数代表此三角形离左侧的字符数
  $ python3 tri_angle.py
  请输入离左侧的距离: 3
  *
 ***
*****
              
14. 打印 1~20的偶数，打印 1~20的奇数

15.打印 1~10的数,打印在一行显示，每个数字用空格分隔
   1 2 3 4 5 6 7 8 9 10
   提示: 用print函数的end参数
              
16. 用while循环生成如下字符串:
   "ABCD.....XYZ"
              
17. 用while循环生成如下字符串
   "AaBbCcDd....XxYyZz"
              
18. 算出 100 ~1000之间的水仙花数(Narcissistic number)

水仙花是指百位的立方+ 十位的立方 + 个位的立方等于原数的数字
例: 153 等于 1**3 + 5**3 + 3**3

答案: 153 370 371 407

              
练习1：
尝试自己实现字符串属性函数(能写多少是多少，目的是锻炼思维)。

练习2：
1，完成一个函数，判断字符串中单词个数。
2，把该字符串中的单词顺序逆序。
	例如：a="This is a pig"
	逆序：a="pig a is This"

练习3：
  输入三行文字 ,让这三行文字在一个方框内居中显示
  如输入(不要输入中文):
  hello tarena!
  my name is weimingze！
  good-bye
  显示结果如下：
+-----------------------+
|     hello tarena!     |
| my name is weimingze! |
|        good-bye       |
+-----------------------+


练习4: 
输入Unicode 的起始编码和终止编码,打印此范围内所有的字符。
  如:

输入起始值:48
输入终止址:64
打印结果如下：
  十进制编码  十六进制编码  文字
    48          0x30      0
    49          0x31      1
    50          0x32      2
输入起始值:10000
输入终止址:10002
打印结果如下：
  十进制编码  十六进制编码  文字
    10000      0x2710     ✐
    10001      0x2711     ✑
    10002      0x2712     ✒

练习5：
判断一个字符串是否回文？
a="123456789987654321"

练习6：
查找两个字符串的最长公共子串。
a="123456789"
b="123312345612345678"
“12345678”
逻辑里一定用到三层循环！！！
	      
练习：
输入三个数，存于列表中，打印出这三个数最大值，最小值和平均值

练习：
  输入任意整数,先判断你输入的数是否为质数(只能被1和自身整除的数),如果为质数，则加入到列表中.再次输入任意整数，再判断.......
  直至输入的数小于等于0为止。
  最后打印您输入的质数。
  (所用知识点：输入输出，死循环，求余，for, range,列表...)

练习：

1. 生成前40个斐波那契数
   1 1 2 3 5 8 ......
   要求将这些数保存在列表中。最后打印这些数
   提示：用 while,for , 序列
2. 完全数:
   完全数是指除自身以外的所有的因数相加之和等于自身的数
   例：
     1 + 2 + 3 = 6
     1,2,3都为6的因数(能被一个数x整除的数为y,则y为x的因数)
     求4~5个完全数并打印出来.
   答案（前三个)
   6
   28
   496

练习：

有字符串"hello", 生成新字符串"h e l l o" 和"h-e-l-l-o"
	      
	      
元组练习：
1.输入任意一个字符串或数字，判断是否为回文
  12321    回文数
  ABCDCBA  回文
  GEAEG    回文
  abeeba   回文

1. 编写程序，获取一个数值，计算并打印其中每个数字出现个数
   如：输入:2234524
   打印如下：
   数字2出现3次
   数字3出现1次
   数字4出现2次
   数字5出现1次

练习：
已知两个等长的列表list1和list2,  以list1中的元素为键，以list2中的元素为值，生成相应字典  如:

```python
list1 = ["a", "b", "c"]
list2 = [1,2,3]
生成字典为:
  {'a':1, 'b':2, 'c' : 3}
```

练习：
　　输入5个学生的姓名和年龄，每个学生的信息形成字典后存入列表，内部存储格式如下：
  [{"name":"aaa", "age": 20}, {"name":"bbb", "age": 30}, ...]
  输入完成后，打印所有学生信息如下：
  +-------------+-------------+
  |    姓名     |   年龄      |
  +-------------+-------------+
  |     aaa     |    20       |
  |     bbb    |    30       |
  |     ...        |    ...        |
  +-------------+-------------+
2.输入学生年龄，把低于此年龄的学生信息打印出来
知识点:
  列表和字典组合使用

集合练习：
  经理有: 曹操 刘备 周瑜
  技术员有: 曹操 周瑜，张飞，赵云
  用集合求:
  1.即是经理也是技术员的人有谁？
  2.是经理，但不是技术员的人都有谁？
  3.是技术员，但不是经理的人有谁？
  4.张飞是经理吗？
  5.身兼一职的人都有谁？
  6.经理和技术员共有几个?

练习：
任意输入一些单词存入集合中，当输入0时结束输入。
打印输入的单词种类数（去重），每个单词打印一次到终端上
提示：可以用len(x)函数求集合长度

练习：

1. （集合/输入输出）
 模拟点名系统，已知全班名单，随机打印学生姓名进行点名，并得到此学生是否已到，输入'y'代表已到,输入'n'代表未到，点名完成后，打印未到者名单

2. 假设有一个列表有很多数据，还有重复的，例如：
 L = [9, 8, 4, 6, 8, 9, 4, 1, ...]
 打印出列表中的数据，要求重复的只打印一次，打印的顺序以列表中第一次现在顺序为准.
 如:上述列表打印：
 9 8 4 6 1 ...
 提示：列表和集合组合使用


	
练习：
定义两个函数:
   sum3(a, b, c) 用于返回三个数的和
   pow3(x)    用于返回x的三次方(立方)
   用以上两个函数计算：

1. 计算1的立方＋２的立方＋３的立方的和
2. 计算1+2+3的和的立方

练习：
  写一个函数sum4(a,b,c,d) 来计算四个参数的和
  可以用如下方法调用：
  print(sum4(1, 2))
  print(sum4(1.1,2.2, 3.3))
  print(sum4(100, 200, 300, 400))

练习:
  写一个函数minmax有不定长个参数,返回这些参数的最大值和最小值(形成元组,最小在前,最大值在后)
  调用此函数,得到最大值和最小值并打印出来

练习：
　　写一个函数，在函数内部读取学生姓名，并存入列表中,通过两种方式返回学生姓名数据并打印出来
　　方式1，通过返回值返回数据
　　方式2，通过参数返回数据

练习:
  prime(质数/素数)

1. 写一个函数isprime(x),判断x是否为素数,如果为素数,返回True,否则返回False.  


1. 写一个函数prime_m2n(m, n) 返回从m开始,到n结束范围内的素数,返回这些质数的列表,并在主程序中打印
   如:
   L = prime_m2n(5, 10)
   print(L)  # [5, 7]
2. 写一个函数primes(n), 返回指定范围内的全部素数的列表,并在主程序中打印这些素数
   L = primes(100)
   print(L)  # [2, 3, 5, 7, ....... 97]

operator(goodbye, ["张三", "李四"])

day7 
练习:
  写一个函数，此函数有一个参数op,如下：
      def get_op(op):
          ...
  此函数在传入字符串"加"，　返回加操作的函数
    def myadd(x, y): return x + y
  此函数在传入字符串"乘"，　返回乘操作的函数
    def mymul(x, y): return x * y
　　在主函数中程序如下：
  a = int(input("输入第一个数:"))
  b = int(input("输入第二个数:"))
  operator = input("请输入操作方式：")
  fn = get_op(operator)
  print("结果是:", fn(a, b))
  测试用例：
  　3
    2
    +<回车>
    结果是:5
  　
  	3
    2
    *<回车>
    结果是:6

练习:
1.给出一个数n,写一个函数来计算1+2+3+.....+n的和
  要求用函数来做
  如:
  print(mysum(100))  # 5050

2. 给出一个数n,写一个函数计算1+2**2+3**3+...+n**n的和
  注意:n不要太大，否则可能溢出

3. 写函数打印杨辉三角(只打印6层)
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1

--------------------------

运算符重载 部分练习

练习 exercise_0901_student_info :

  自定义一个类Student类,有学生姓名,年龄,成绩

  class Student:

      ....

  L = []

  s1 = Student("张三", 21, 98)

  L.append(s1)

  s1 = Student("李四", 20, 88)

  L.append(s1)

  for x in L:

      print(x) # 等同于: x.infos()
 
	
	
练习：

实现一个mystring类，重载<<和>>,分布实现字符串循环左右移动：
```python
class MyString:
	pass

a = MyString('123456789')
a = a<< 2
print(a)	# a= '345678912'
```

练习 exercise_0902:

自定义一个类MyList,实现+ += * *= 操作

实现能够用len(x)返回自定义列表的元素个数

练习 exercise_0903 :

实现有序集合OrderSet类,能实现两个集合的 交集(&),并集 |,补集(-), 对称补集(^) ,==, != 等操作

功能与集合相同,但数据有先后顺序,要求内部用列表来存储


练习 exercise_0904  ：

　　定义一个表示素数的类:

  class Primes:

     def init(self, end):

     　　　"""end 用于表示素数的终止点

           素数的起始点是2(包含2)

        """

        ...

  用此类创建一个对象:

     p1 = primes(100)

     if 50 in p1:

        print("50是素数")

     else:

        print("50不是素数")

练习  exercise_0905 ：

  将index_slice.py 修改方法：
```
setitem(self, index, value):

myl = MyList(5, 1)  # MyList([1, 1, 1, 1, 1])

myl[1] = 2

myl[2] = 3

myl[3] = 4

myl[4] = 5

print(myl)  # MyList([1, 2, 3, 4, 5])

myl[::2] = 10

print(myl)  # MyList([10, 2, 10, 4, 10])
```

练习:

1. 输入圆的半径r和圆的角度d, 算出圆的扇形的面积
2. 写一个程序打印出一个电子时钟,格式为:
   HH:MM:SS 格式
   17:27:23
   每隔一秒钟,打印刷新一次
3. 编写一个闹钟程序,启动时设置定时时间,到时间后打印一句话,然后退出程序

练习:

  猜数字游戏程序:

    随机生成一个0~100之间的一个整数,保存在变量x内
    让用户输入一个数y,输出猜数字的结果:
      如果y等于x,提示"恭喜你猜对了",并退出程序
      如果y大于x,提示"您猜的数大了", 并让用户继续猜
      如果y小于x,提示"您猜的数小了",继续猜
    直到猜对为止退出程序，并显示用户猜数字的次数

    练习：

　　把昨天写的练习相应的函数写个一个模块叫day12.py

  再写一个主模块来调用相应的函数．

练习：

已知有五位朋友在一起

第五位朋友比第四位大2岁

第四位朋友比第三位大2岁

第三位朋友比第二位大2岁

第二位朋友比第一位大2岁

第一位朋友　说他10岁

试写程序算出第五位朋友几岁

试用递归完成

模拟斗地主发牌

扑克片共54张

黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665'),桃('\u2666')

A2-10JQK

大小王

三个人，每个人发17张牌，底牌留三张：

输入回车,打印第１个人的17张牌

输入回车,打印第２个人的17张牌

输入回车,打印第３个人的17张牌

输入回车,打印三张底片牌

猜　数字游戏2

  有0-9十个数字，分别放在四个盒子内(列表中放四个元素，不能重复)

  [4, 6, 0, 3]

  让用户每次输入四个数字

  4603<回车>  输出全对,程序结束

  4601<回车>

  输出:3A0B (A代表位置对，数字也对, B代对数字对，位置不对)

  1046<回车>

  输出:0A3B

  直到猜对为止

===================================================================

课堂练习:

将如下数据写入到文件data.txt中,数据如下:

张某某 13845679876

李某某 13899999999

赵某某 13088888888

写程序读取数据,打印出姓名和电话号码



练习:

1. 写一个生成器函数,用来生成斐波那契数列的前n个数
   def fibonacci(n):
     ....
   例:
       for x in fibonacci(7):
       print(x, end= ' ') # 1 1 2 3 5 8 13
2. 写一个程序,输入任意多人的名字,电话号码,住址存入"info.txt"中
   文件格式自己定义,完成后查看文件格式是不是你要的格式
3. 写一个程序,读入"info.txt", 中的内容,以表格形式打印这些内容 
4. 为学生管理的程序添加保存学生信息和打开学生信息功能
   7) 保存学生信息
   8) 打开已存的学生信息

练习:

写一个程序从键盘输入一段字符串,将其字符串转换为字节串(bytes)后计算长度并打印此字节串,然后将此字节串再转换为字符串, 比较此字符串是否与先前输入的字符串相同?

练习:有一个bytearray字节序列:

   ba=bytearray(b'a1b2c3d4')

   如何得到字符串 '1234'和'abcd'

   将上述bytearray改为bytearray(b'A1B2C3D4')

练习：

　　 图形类Shape有方法：

　　　　　　draw(self)  画图形

      move(self, offx, offy)  将图形移动从标系的(offx,offy) 位置

再定点类Point, 圆类Circle, 线类Line, 矩形类Ractange 直接或间接继承自Shape类

所有的类方法有　draw, move

属性如下：

点:  x, y

圆:  x, y, r(半径)

线类  x, y, x2, y2

矩形：　x, y, width(宽), height(高)

用这些类创建一些对象放入列表中:

如：

    docs = [Point(1, 2), Circel(3,4,5), 
    Line(6,7,8,9),
    Ractange(10, 20, 50, 100)]
    for x in docs:
    x.draw()
    让所有图形都向右移动10个像素,向下移动20个像素
    for x in docs:
    x.move(10, 20) 
    再次打印图形:
    for x in docs:
    x.draw()
    class Circel:
    def draw(self):
       print("圆(", self.x, self.y, self.r, ")")


