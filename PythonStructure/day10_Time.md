内置模块:
  builtins, sys, time, itertools ...., math

标准库模块
  random, datetime, os, xml ....

http://docs.python.org

=============================================================

# 时间模块 time

此模块提供了时间相关的函数，且一直可用

导入方式:

```python
import time
from time import *
from time import xxx
```

## 时间简介:

  公元纪年是公元0000年1月1日开始

  对于Unix/Linux系统 ,计算机元年是从1970-1-1 零时开始的，此时时间为0

  UTC时间(Coordinated Universal Time) 是从Greenwich时间开始计算的.

  UTC时间不会因时区问题而产生错误

  DST阳光节约时间(Daylight Saving Time), 又称夏令时,是经过日照时间修正后的时间

## 时间元组

是一个9个整数组成的,这九个元素自前至后依次为:

四位的年(如:1993)

月(1-12)
日(1-31)
时(0-23)
分(0-59)
秒(0-59)
星期几(0-6, 周一是0)
元旦开始日(1-366)
夏令时修正时间(-1, 0 或 1)

注:如果年份小于100,则会自动转换为加上1900后的值

## 时间模块中的变量和函数

### 变量

- time.timezone  本地区时间与UTC时间差(秒为单位)
- time.altzone   夏令时时间与UTC时间差(秒为单位)
- time.daylight  夏令时校正时间
- time.tzname    时区名称的元组

### 函数:

- time.time()  返回从计算机元年至当前时间的秒数的浮点数(UTC时间为准)
- time.sleep(secs)  让程序按给定的秒数睡眠一段时间
- time.gmtime([secs]) 将给定的秒数转换为UTC表达的时间元组
- time.mktime(tuple)  将时间元组转换为新纪元秒数时间(UTC为准)
- time.asctime([tuple]) 将时间元组转换为字符串
- time.localtime([secs]) 将UTC秒数转换为时间元组(以本地时间为准)
- time.clock()  返回自CPU开始运行到现在的时间秒数的浮点数

[] 里的内容代表可省略

课堂练习:
  写一个程序,输入出生日期,算出你已经出生多少天?