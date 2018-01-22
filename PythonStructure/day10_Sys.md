# 系统模块 sys

与系统相关的信息

### 数据:

sys.path 模块搜索路径 path[0] 是当前脚本程序的路径名,或者是''
sys.modules  已加载模块的字典
sys.version  版本信息
sys.version_info  版本信息的命名元组
sys.argv     命令行参数 argv[0] 代表当前脚本程序路径名
sys.copyright  获取python版权相关信息
sys.builtin_module_names  获得python内建模块名称(字符串元组)

sys.argv示例见：myprog.py

练习：
　　写一个程序myadd.py 然后执行此程序
  如果执行如下命令:
  $ ./myadd.py
  用法: ./myadd.py 　数字 运算符 数字

  $ ./myadd.py  5 加 2
  结果是: 7
  $ ./myadd.py  5 乘 2
  结果是: 10 

### 函数

sys.exit([code])  退出程序，正常退出时sys.exit(0)
sys.getrecursionlimit()  得到递归的层次限制值
sys.setrecursionlimit(n) 设置递归的最大层次限制值

## 标准库模块

### 随机模块 random

#### 假设导入:

import random as R

#### 函数:

R.random()    返回一个[0,1) 之间的随机数
R.getrandbits(nbit)   以长整型的形式返回用nbit位来表示的随机数
R.uniform(a,b)  返回[a, b) 区间内的随机数
R.randrange([start, ] stop [, step]) 返回range(start, stop, step)中的随机数)
R.choice(seq)  从序列中返回随意元素
R.shuffle(seq) 随机指定序列的顺序(乱序序列)
R.sample(seq, n)  从序列中选择n个随机且不重复的元素

例:
import random as R
print(R.random())