# 迭代器 Iterator 和 生成器 Generator

什么是迭代器:
  迭代器是指能用next(it)函数取值的对象(实例)。


可以直接作用于for循环的对象统称为可迭代对象(Iterable):
例:
>>> L = [1,2,3]
>>> for i in L:
>>> ...		print(i)
>>> ...
>>> 1
>>> 2
>>> 3

所有的Iterable均可以通过内置函数iter()来转变为Iterator：
>>> I=iter(L)
>>> type(I)
>>> <class 'list_iterator'>

所有的Iterable都可以使用next()进行遍历访问：
>>> next(I)
>>> 1
>>> next(I)
>>> 2
>>> next(I)
>>> 3

如果迭代器的元素是有限的，那么访问最后时，如果继续next会出现StopIteration异常：
>>> next(I)
>>> Traceback (most recent call last):
>>>   File "<stdin>", line 1, in <module>
>>> StopIteration


可迭代对象并不是迭代器，如果使用next会报错：
>>> next(L)
>>> Traceback (most recent call last):
>>>   File "<stdin>", line 1, in <module>
>>> TypeError: 'list' object is not an iterator

函数:
iter(x)  从一个对象x中返回一个迭代器,x必须是能提供一个迭代器的对象
next(it)  从迭代器it中获取下一个记录,如果无法获取下一条记录则触发StopIteration异常

注：range和xrang区别
python2中，range和xrange返回的都是可迭代对象，但是类型不同：
>>> type(range(10))
>>> <type 'list'>
>>> type(xrange(10))
>>> <type 'xrange'>

python3中，xrange更名为range,原range被替换：
>>> type(range(10))
>>> <class 'range'>
>>> type(xrange(10))
>>> Traceback (most recent call last):
>>>   File "<stdin>", line 1, in <module>
>>> NameError: name 'xrange' is not defined


示例:见iterator.py
it = iter(range(1, 10, 3))  # 1, 4, 7
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it)) #
except StopIteration:
    print("迭代器取值结束")

# 打印1~10之间的奇数
it = iter(range(1, 10, 2))
try:
    while True:
        print(next(it))

except StopIteration:
    print("打印结束")


说明:
  用iter函数可返回一个可迭代对象的迭代器
  迭代器是访问可迭代对象的一种 方式
  迭代器只能往前,不会后退

----------------------------------------------------------
迭代工具函数:
  作用是生成一个个性化的可迭代对象

enumerate(iterable[, start]) 生成带索引的迭代器,返回的迭代类型为索引-值对(index-value)对,默认索引从零开始, 也可以用start指定

示例:见enumerate.py
names = ["张飞", "关羽", "孔明"]

for no, n in enumerate(names, 10001):
    print("第", no, "号人物是:", n)
    # (10001, "张飞")
    # (10002, "关羽")
    # ...


zip(iter1[,iter2[,...]])  返回一个zip对象,此对象用于生成一个元组,此元组的个数由最小的可迭代对象决定

示例:见zip.py
numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']

zip_obj = zip(numbers, names)
for no, name in zip_obj:
    print(name, "的客服电话是:", no)
    # (10086, "中国移动")
    # (10000, "中国电信")

# zip应用案列, 生成字典
d = dict(zip(numbers, names))
print(d)


练习:
  用生成器函数,生成素数, 给出起始值begin和终止值stop
  生成器函数为:
  def primes(begin, stop):
      ....
  如果 [x for x in primes(10, 20)] 将得到列表:
    [11, 13, 17, 19]
------------------------------------------------------------
迭代器协议:
  迭代器协议,是指对象(实例)能够使用next函数获取下项数据,在没有下一项数据时触发一个StopIteration异常来终止迭代的约定。

next(it)  对应 __next__(self) 方法
iter(obj)  对应 __iter__(self) 方法,通常返回一个可迭代对象

示例见: list_iterator.py
L=[1,2,3]

for i in L:
    print(i)


di = L.__iter__()

while True:
    try:
        print(di.__next__())
    except StopIteration:
        print('raise StopIteration')
        break

示例：mylist_iterator.py
class mylist:
    def __init__(self, d):
        self.data = d.copy()
        self.index=0
    
    def __iter__(self):
        if len(self.data) > 0:
            self.index = 0
        else:
            self.index = -1
        return self
    
    def __next__(self):
        if self.index <0 or self.index>= len(self.data):
            raise StopIteration
        else:
            self.index +=1
            return self.data[self.index-1]  



L = mylist([1,2,3])


for i in L:
    print(i)


di = L.__iter__()

while True:
    try:
        print(di.__next__())
    except StopIteration:
        break


for语句和推导式,先调用iter(obj)拿出迭代器,再迭代


练习:
  1. 迭代器协议练习:
      写一个实现迭代器协议的类,让此类可以生成从b开始,到e结束的全部素数
        class Primes:
      def __init__(self, b, e):
        ...
      def __iter__(self): 
      	...
      def __next__(self):
      	...

  L = x for x in Primes(10, 20)
  print(L)  # [ 11, 13, 17, 19]
  prms = Primes(40, 100)
  for x in range(30, 50)
      if x in prms:
          print("x是prms里的素数")

  2. 写一个实现迭代器协议的类,让此类可以生成前n个斐波那契数列
    class Fibonacci:
        def __init__(self, n):
            ...
      def __iter__(self): 
      	...
      def __next__(self):
      	...

    for x in Fibonacci(8):
       print(x)  # 1 1 2 3 5 ...

    print("前10个斐波那契数的和为:", sum(Fibonacii(10)))

    ​

------------------------------------------------------------