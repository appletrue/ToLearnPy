# itertools- 为高效循环创建迭代器的函数

**itertools 模块提供了很多用于产生多种类型迭代器的函数，它们的返回值不是 list，而是迭代器。只有用for循环迭代(或使用 next() 来取值),当迭代至某个值时，它才会被真正计算。**

基于迭代器的代码比使用列表的代码提供更好的内存消耗特性。由于数据不是从迭代器产生的，直到需要时，所有的数据都不需要同时存储在内存中。这种“懒惰”的处理模式可以减少大型数据集的交换和其他副作用，提高性能。

无限迭代器：生成一个无限序列，比如自然数序列 1, 2, 3, 4, ...；
有限迭代器：接收一个或多个序列（sequence）作为参数，进行组合、分组和过滤等；
组合生成器：序列的排列、组合，求序列的笛卡儿积等；

## 无限迭代器

itertools 模块提供了三个函数（事实上，它们是类）用于生成一个无限序列迭代器：

- count(firstval=0, step=1)

  创建一个从 firstval (默认值为 0) 开始，以 step (默认值为 1) 为步长的的无限整数迭代器

- cycle(iterable)

  对 iterable 中的元素反复执行循环，返回迭代器

- repeat(object [,times]

  反复生成 object，如果给定 times，则重复次数为 times，否则为无限

下面，让我们看看一些例子。

### count

`count()` 接收两个参数，第一个参数指定开始值，默认为 0，第二个参数指定步长，默认为 1：

```python
import itertools

nums = itertools.count()
for i in nums:
    if i > 6:
        break
    print(i)
#输出结果:
0
1
2
3
4
5
6
nums = itertools.count(10, 2)    # 指定开始值和步长
for i in nums:
     if i > 20:
         break
     print i
#输出结果:
10
12
14
16
18
20
```

### cycle

`cycle()` 用于对 iterable 中的元素反复执行循环：

```python
import itertools

cycle_strings = itertools.cycle('ABC')
i = 1
for string in cycle_strings:
    if i == 10:
        break
    print(i, string)
    i += 1
#输出结果:
1 A
2 B
3 C
4 A
5 B
6 C
7 A
8 B
9 C
```

### repeat

`repeat()` 用于反复生成一个 object：

```python
import itertools

for item in itertools.repeat('hello world', 3): #打印'hello world' 3遍
   print(item)

for item in itertools.repeat([1, 2, 3, 4], 3):
	print(item)
#输出结果:
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
```

## 有限迭代器

itertools 模块提供了多个函数（类），接收一个或多个迭代对象作为参数，对它们进行组合、分组和过滤等：

| 函数             | 形式                                       | 说明                                       |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| chain()        | chain(iterable1, iterable2, iterable3, ...) | 接收多个可迭代对象作为参数，将它们『连接』起来，作为一个新的迭代器返回。     |
|                | chain.from_iterable(iterable)            | 接收一个可迭代对象作为参数，返回一个迭代器                    |
| compress()     | compress(data, selectors)                | 对数据进行筛选，当 selectors 的某个元素为 true 时，则保留 data 对应位置的元素，否则去除 |
| dropwhile()    | dropwhile(predicate, iterable)           | predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则丢弃该元素，否则返回该项及所有后续项 |
| groupby()      | groupby(iterable[, keyfunc])             | iterable 是一个可迭代对象，keyfunc 是分组函数，用于对 iterable 的连续项进行分组，如果不指定，则默认对 iterable 中的连续相同项进行分组，返回一个 `(key, sub-iterator)` 的迭代器 |
| ifilter()      | ifilter(function or None, sequence)      | 将 iterable 中 function(item) 为 True 的元素组成一个迭代器返回，如果 function 是 None，则返回 iterable 中所有计算为 True 的项 |
| ifilterfalse() | ifilterfalse(function or None, sequence) | 将 iterable 中 function(item) 为 False 的元素组成一个迭代器返回，如果 function 是 None，则返回 iterable 中所有计算为 False 的项 |
| islice()       | islice(iterable, [start,] stop [, step]) | iterable 是可迭代对象，start 是开始索引，stop 是结束索引，step 步长，start 和 step 可选 |
| imap()         | imap(func, iter1, iter2, iter3, ...)     | 返回一个迭代器，元素为 `func(i1, i2, i3, ...)`，`i1`，`i2` 等分别来源于 `iter`, `iter2` |
| starmap()      |                                          |                                          |
| tee()          | tee(iterable [,n])                       | 用于从 iterable 创建 n 个独立的迭代器，以元组的形式返回，n 的默认值是 2 |
| takewhile()    | takewhile(predicate, iterable)           | predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则保留该元素，只要 predicate(item) 为 false，则立即停止迭代 |
| izip()         | izip(iter1, iter2, ..., iterN)           | 用于将多个可迭代对象**对应位置**的元素作为一个元组，将所有元组『组成』一个迭代器，并返回, 如果某个可迭代对象不再生成值，则迭代停止 |
| izip_longest() | izip_longest(iter1, iter2, ..., iterN, [fillvalue=None]) | 跟 `izip` 类似，但迭代过程会持续到所有可迭代对象的元素都被迭代完, 如果有指定 fillvalue，则会用其填充缺失的值，否则为 None |

chain 举例:

chain(iterable1, iterable2, iterable3, ...)

接收多个可迭代对象作为参数，将它们『连接』起来，作为一个新的迭代器返回。

```python
from itertools import chain

for item in chain([1, 2, 3], ['a', 'b', 'c']):
     print item
#输出结果:
1
2
3
a
b
c
```

`chain` 还有一个常见的用法：

```
chain.from_iterable(iterable)
```

接收一个可迭代对象作为参数，返回一个迭代器：

```
from itertools import chain

string = chain.from_iterable('ABCD')
string.next()
'A'
```

### compress

`compress` 的使用形式如下：

```
compress(data, selectors)
```

`compress` 可用于对数据进行筛选，当 selectors 的某个元素为 true 时，则保留 data 对应位置的元素，否则去除：

```
from itertools import compress

list(compress('ABCDEF', [1, 1, 0, 1, 0, 1]))			#['A', 'B', 'D', 'F']
list(compress('ABCDEF', [1, 1, 0, 1]))					#['A', 'B', 'D']
list(compress('ABCDEF', [True, False, True]))			#['A', 'C']
```

### dropwhile

`dropwhile` 的使用形式如下：

```
dropwhile(predicate, iterable)
```

其中，predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则丢弃该元素，否则返回该项及所有后续项。

```
from itertools import dropwhile

list(dropwhile(lambda x: x < 5, [1, 3, 6, 2, 1]))		#[6, 2, 1]
list(dropwhile(lambda x: x > 3, [2, 1, 6, 5, 4]))		#[2, 1, 6, 5, 4]
```

### groupby

`groupby` 用于对序列进行分组，它的使用形式如下：

```
groupby(iterable[, keyfunc])
```

其中，iterable 是一个可迭代对象，keyfunc 是分组函数，用于对 iterable 的连续项进行分组，如果不指定，则默认对 iterable 中的连续相同项进行分组，返回一个 `(key, sub-iterator)` 的迭代器。

```
from itertools import groupby

for key, value_iter in groupby('aaabbbaaccd'):
     print key, ':', list(value_iter)
#输出结果:
a : ['a', 'a', 'a']
b : ['b', 'b', 'b']
a : ['a', 'a']
c : ['c', 'c']
d : ['d']
>>>
data = ['a', 'bb', 'ccc', 'dd', 'eee', 'f']
for key, value_iter in groupby(data, len):    # 使用 len 函数作为分组函数
     print key, ':', list(value_iter)
#输出结果:
1 : ['a']
2 : ['bb']
3 : ['ccc']
2 : ['dd']
3 : ['eee']
1 : ['f']
>>>
data = ['a', 'bb', 'cc', 'ddd', 'eee', 'f']
for key, value_iter in groupby(data, len):
     print key, ':', list(value_iter)
#输出结果:
1 : ['a']
2 : ['bb', 'cc']
3 : ['ddd', 'eee']
1 : ['f']
```

## ifilter

`ifilter` 的使用形式如下：

```
ifilter(function or None, sequence)
```

将 iterable 中 function(item) 为 True 的元素组成一个迭代器返回，如果 function 是 None，则返回 iterable 中所有计算为 True 的项。

```
from itertools import ifilter

list(ifilter(lambda x: x < 6, range(10)))		#[0, 1, 2, 3, 4, 5]
list(ifilter(None, [0, 1, 2, 0, 3, 4]))			#[1, 2, 3, 4]
```

`ifilterfalse` 的使用形式和 `ifilter` 类似，它将 iterable 中 function(item) 为 False 的元素组成一个迭代器返回，如果 function 是 None，则返回 iterable 中所有计算为 False 的项。

```
from itertools import ifilterfalse

list(ifilterfalse(lambda x: x < 6, range(10)))		#[6, 7, 8, 9]
list(ifilter(None, [0, 1, 2, 0, 3, 4]))				#[0, 0]
```

## islice

`islice` 是切片选择，它的使用形式如下：

```
islice(iterable, [start,] stop [, step])
```

其中，iterable 是可迭代对象，start 是开始索引，stop 是结束索引，step 是步长，start 和 step 可选。

```
from itertools import count, islice

list(islice([10, 6, 2, 8, 1, 3, 9], 5))		#[10, 6, 2, 8, 1]

list(islice(count(), 6))			#[0, 1, 2, 3, 4, 5]
list(islice(count(), 3, 10))		#[3, 4, 5, 6, 7, 8, 9]
list(islice(count(), 3, 10 ,2))		#[3, 5, 7, 9]
```

## imap

`imap` 类似 `map` 操作，它的使用形式如下：

```
imap(func, iter1, iter2, iter3, ...)
```

`imap` 返回一个迭代器，元素为 `func(i1, i2, i3, ...)`，`i1`，`i2` 等分别来源于 `iter`, `iter2`。

```
from itertools import imap

imap(str, [1, 2, 3, 4])						#<itertools.imap object at 0x10556d050>
list(imap(str, [1, 2, 3, 4]))					#['1', '2', '3', '4']
list(imap(pow, [2, 3, 10], [4, 2, 3]))			#[16, 9, 1000]
```

## tee

`tee` 的使用形式如下：

```
tee(iterable [,n])
```

`tee` 用于从 iterable 创建 n 个独立的迭代器，以元组的形式返回，n 的默认值是 2。

```
>>> from itertools import tee
>>>
>>> tee('abcd')   # n 默认为 2，创建两个独立的迭代器
(<itertools.tee object at 0x1049957e8>, <itertools.tee object at 0x104995878>)
>>>
>>> iter1, iter2 = tee('abcde')
>>> list(iter1)
['a', 'b', 'c', 'd', 'e']
>>> list(iter2)
['a', 'b', 'c', 'd', 'e']
>>>
>>> tee('abc', 3)  # 创建三个独立的迭代器
(<itertools.tee object at 0x104995998>, <itertools.tee object at 0x1049959e0>, <itertools.tee object at 0x104995a28>)
```

## takewhile

`takewhile` 的使用形式如下：

```
takewhile(predicate, iterable)
```

其中，predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则保留该元素，只要 predicate(item) 为 false，则立即停止迭代。

```
>>> from itertools import takewhile
>>>
>>> list(takewhile(lambda x: x < 5, [1, 3, 6, 2, 1]))
[1, 3]
>>> list(takewhile(lambda x: x > 3, [2, 1, 6, 5, 4]))
[]
```

## izip

`izip` 用于将多个可迭代对象**对应位置**的元素作为一个元组，将所有元组『组成』一个迭代器，并返回。它的使用形式如下：

```
izip(iter1, iter2, ..., iterN)
```

如果某个可迭代对象不再生成值，则迭代停止。

```
>>> from itertools import izip
>>> 
>>> for item in izip('ABCD', 'xy'):
...     print item
...
('A', 'x')
('B', 'y')
>>> for item in izip([1, 2, 3], ['a', 'b', 'c', 'd', 'e']):
...     print item
...
(1, 'a')
(2, 'b')
(3, 'c')
```

`izip_longest` 跟 `izip` 类似，但迭代过程会持续到所有可迭代对象的元素都被迭代完。它的形式如下：

```
izip_longest(iter1, iter2, ..., iterN, [fillvalue=None])
```

如果有指定 fillvalue，则会用其填充缺失的值，否则为 None。

```
>>> from itertools import izip_longest
>>>
>>> for item in izip_longest('ABCD', 'xy'):
...     print item
...
('A', 'x')
('B', 'y')
('C', None)
('D', None)
>>>
>>> for item in izip_longest('ABCD', 'xy', fillvalue='-'):
...     print item
...
('A', 'x')
('B', 'y')
('C', '-')
('D', '-')
```

## 组合生成器

itertools 模块还提供了多个组合生成器函数，用于求序列的排列、组合等：

| 函数                            | 形式                                       | 说明                                       |
| ----------------------------- | ---------------------------------------- | ---------------------------------------- |
| product                       | product(iter1, iter2, ... iterN, [repeat=1]) | 用于求多个可迭代对象的笛卡尔积，它跟嵌套的 for 循环等价           |
| permutations                  | permutations(iterable[, r])              | 用于生成一个排列, r 指定生成排列的元素的长度，如果不指定，则默认为可迭代对象的元素长度 |
| combinations                  | combinations(iterable, r)                | 用于求序列的组合 ，r 指定生成组合的元素的长度                 |
| combinations_with_replacement |                                          | 和 `combinations` 类似，但它生成的组合包含自身元素        |

### product

`product` 用于求多个可迭代对象的笛卡尔积，它跟嵌套的 for 循环等价。它的一般使用形式如下：

```
product(iter1, iter2, ... iterN, [repeat=1])
```

其中，repeat 是一个关键字参数，用于指定重复生成序列的次数，

```
from itertools import product

for item in product('ABCD', 'xy'):
     print(item)

('A', 'x')
('A', 'y')
('B', 'x')
('B', 'y')
('C', 'x')
('C', 'y')
('D', 'x')
('D', 'y')
list(product('ab', range(3)))
[('a', 0), ('a', 1), ('a', 2), ('b', 0), ('b', 1), ('b', 2)]

list(product((0,1), (0,1), (0,1)))
[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

list(product('ABC', repeat=2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

### permutations

`permutations` 用于生成一个排列，它的一般使用形式如下：

```
permutations(iterable[, r])
```

其中，r 指定生成排列的元素的长度，如果不指定，则默认为可迭代对象的元素长度。

```
from itertools import permutations

permutations('ABC', 2)
<itertools.permutations object at 0x1074d9c50>

list(permutations('ABC', 2))
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

list(permutations('ABC'))
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

```

### combinations

`combinations` 用于求序列的组合，它的使用形式如下：

```
combinations(iterable, r)
```

其中，r 指定生成组合的元素的长度。

```
from itertools import combinations

list(combinations('ABC', 2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

`combinations_with_replacement` 和 `combinations` 类似，但它生成的组合包含自身元素。

```
from itertools import combinations_with_replacement
list(combinations_with_replacement('ABC', 2))
#输出结果:
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

```

# 


“无限”迭代器：

>>> import itertools
>>> natuals = itertools.count(1)
>>> for n in natuals:
...     print n
...
1
2
3
...
因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

cycle()会把传入的一个序列无限重复下去：

>>> import itertools
>>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
>>> for c in cs:
...     print c
...
'A'
'B'
'C'
'A'
'B'
'C'
...
同样停不下来。

repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

>>> ns = itertools.repeat('A', 10)
>>> for n in ns:
...     print n
...
打印10次'A'
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：

>>> natuals = itertools.count(1)
>>> ns = itertools.takewhile(lambda x: x <= 10, natuals)
>>> for n in ns:
...     print n
...
打印出1到10
itertools提供的几个迭代器操作函数更加有用：

chain()
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

for c in itertools.chain('ABC', 'XYZ'):
    print c
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
groupby()
groupby()把迭代器中相邻的重复元素挑出来放在一起：

>>> for key, group in itertools.groupby('AAABBBCCAAA'):
...     print key, list(group) # 为什么这里要用list()函数呢？
...
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
imap()
imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。

>>> for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
...     print x
...
10
40
90
注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕：

>>> r = map(lambda x: x*x, [1, 2, 3])
>>> r # r已经计算出来了
[1, 4, 9]
当你调用imap()时，并没有进行任何计算：

>>> r = itertools.imap(lambda x: x*x, [1, 2, 3])
>>> r
<itertools.imap object at 0x103d3ff90>
# r只是一个迭代对象
必须用for循环对r进行迭代，才会在每次循环过程中计算出下一个元素：

>>> for x in r:
...     print x
...
1
4
9
这说明imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样能够实现惰性计算的函数就可以处理无限序列：

>>> r = itertools.imap(lambda x: x*x, itertools.count(1))
>>> for n in itertools.takewhile(lambda x: x<100, r):
...     print n
...
结果是什么?
如果把imap()换成map()去处理无限序列会有什么结果？

>>> r = map(lambda x: x*x, itertools.count(1))
结果是什么?
ifilter()
不用多说了，ifilter()就是filter()的惰性实现。
---------
[官方文档](https://docs.python.org/3.6/library/itertools.html)    
[高效的 itertools 模块](http://funhacks.net/2017/02/13/itertools/)    
[PyMOTW-3](https://pymotw.com/3/itertools/index.html#module-itertools)
