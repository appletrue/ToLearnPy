# 运算符重载

- 什么是运算符重载:

用自定义的规则实现实例之间的运算符操作或函数操作

- 作用:

让实例像数学表达式一样的进行运算操作

让实例像内建对象一样进行内建函数操作

让程序简洁易读

```Python
def add(a,b):
	return a+b

a = '123'
b = '456'
c = add(a,b)
print(c)  # #c = '123456'

def +(a,b)：  #SyntaxError: invalid syntax??2.7?
    return a+b

a = '123'
b = '456'

c = a+b  	#c = '123456'
```
## 对象转字符串函数重载

### repr(obj)

对象转字符串函数重载方法: repr() 函数的重载方法:

```python
def repr(self):
    ...
```
### str(obj)

对象转字符串函数重载方法: str() 函数的重载方法:

```python
def str(self):
    ....
```
注:如果对象没有str方法,则用repr(obj)函数的结果代替

示例见:  mynumber.py
```python
class MyNumber:

"此类用于定义一个整型数字类, 用于演示str函数重载"

def init(self, value):
    self.data = value

def repr(self):
    print("repr被调用")
    return "MyNumber(" + repr(self.data) + ")"

def str(self):
    print("str被调用")
    return "整数数值(" + str(self.data) +")"

n1 = MyNumber(100)
n2 = MyNumber(200)
print(repr(n1))  # 'MyNumber(100)'
print(str(n2))   # MyNumber(200)
print(n2)  # 等同于print(str(n2))
print(n1) # print(str(n1))
```

## 算术运算符的重载:

  ``+ ``     add

  ``-``      sub

  ``*``      mul

  ``/``      truediv

  ``//``     floordiv

  ``% ``     mod

  ``**``     pow

### 二元运算符重载的格式:

```python
  def xxx(self, other):
      ....
```
注:  二元运算符的重载方法的参数列表中只能有两个参数

- 重载说明:

  - 运算符重载方法的参数已经有固定的含义,不可改变原有意义
  - 除 call 方法外,其它重载方法的参数个数不可改变

示例: （mylist.py）  自定义一个列表类.实现该类两个实例的相加运算（等价于拼接）

```python
class MyList:

def init(self, a):
    self.data = a.copy()

def infos(self):
    return "MyList(" + str(self.data) + ")"

def str(self):
    return self.infos()

def myadd(self, other):
    r = []
    r.extend(self.data)
    if type(other) == int:
        r.append(other)
    elif type(other) == MyList:
        r.extend(other.data)
    else:
        raise ValueError("other 不允许为其它值")
    # self.data.clear()
    # other.data.clear()
    return MyList(r)

def add(self, other):
    return self.myadd(other)

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1.myadd(L2)
print("L1=", L1)
print("L2=", L2)
L3 = L1 + L2
print("L3=", L3)  # MyList([1,2,3,4,5,6])
L3 = L2 + L1
print(L3)  # MyList([4,5,6,1,2,3])
L3 = L1 + 10
print(L3)  # MyList([1,2,3,10])
```

## 反向算术运算符重载:

| 运算符                  | 说明               |
| -------------------- | ---------------- |
| radd(self, lhs)      | 加法 lhs + self    |
| rsub(self, lhs)      | 减法 lhs - self    |
| rmul(self, lhs)      | 乘法 lhs * self    |
| rtruediv(self, lhs)  | 除法 lhs / self    |
| rfloordiv(self, lhs) | 地板除 lhs // self  |
| rmod(self, lhs)      | 取模(求余)lhs % self |
| rpow(self, lhs)      | � lhs ** self   |
| lhs(left hand side)  | 左手边              |

示例见:mylist2.py

```python
class MyList:

def init(self, a):
    self.data = a.copy()

def infos(self):
    return "MyList(" + str(self.data) + ")"

def str(self):
    return self.infos()

def myadd(self, other):
    r = []
    r.extend(self.data)
    if type(other) == int:
        r.append(other)
    elif type(other) == MyList:
        r.extend(other.data)
    else:
        raise ValueError("other 不允许为其它值")

    # self.data.clear()
    # other.data.clear()
    return MyList(r)
# def add(self, other):
#     return self.myadd(other)

def mul(self, rhs):  # right hand side
    return MyList(self.data * rhs)

# 以下方法可以被替代

# L0 = MyList([])
# for x in range(rhs):
#     L0 += MyList(self.data)
#     # L0 = L0 + MyList(self.data)
# return L0

def rmul(self, lhs):
    # return MyList(self.data * lhs)
    # return self * lhs
    return self.mul(lhs)

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 * 3
print(L3)
L3 = 3 * L1  # 调用L1.rmul(3)
print(L3)  # ??????
```

## 复合赋值算术运算符:

| 复合赋值算术运算符            | 说明                |
| -------------------- | ----------------- |
| iadd(self, rhs)      | 加法 self += rhs    |
| isub(self, rhs)      | # 减法 self -= rhs  |
| imul(self, rhs)      | # 乘法 self *= rhs  |
| itruediv(self, rhs)  | # 除法 self /= rhs  |
| ifloordiv(self, rhs) | 地板除 self //= rhs  |
| imod(self, rhs)      | 取模(求余)self %= rhs |
| ipow(self, rhs)      | � self **= rhs   |

示例见:mylist3.py

```python
class MyList:

def init(self, a):
    self.data = a.copy()

def str(self):
    return "MyList(" + str(self.data) + ")"

def mul(self, rhs):  # right hand side
    print("mul")
    return MyList(self.data * rhs)

def imul(self, rhs):
    print("imul")
    self.data = self.data * rhs
    return self

L1 = MyList([1, 2, 3])
# L1 = L1 * 2
L1 *= 2
print(L1)
```

## 一元运算符的重载:

| 运算符    | 说明    |
| ------ | ----- |
| neg    | -(负号) |
| pos    | +(正号) |
| invert | ~(取反) |

- 重载方法:
```python
def xxx(self):
   ...
```
示例见:mylist4.py

```python
class MyList:

    def init(self, a):
        self.data = a.copy()

    def str(self):
        return "MyList(" + str(self.data) + ")"

    def neg(self):
        ml = MyList(self.data)
        for i in range(len(ml.data)):
            ml.data[i] = -ml.data[i]
        return ml

    def invert(self):
        ml = MyList(self.data)
        ml.data.reverse() # ml.data = [3,2,1]
        return ml

L1 = MyList([1, 2, 3])
L2 = -L1
print("L2=", L2)  # MyList([-1, -2, -3])
L3 = ~L1
print(L3)  # MyList([3, 2, 1])
```

## 比较运算符的重载:比较运算的通常用于返回True和False

| 运算符  | 说明              |
| ---- | --------------- |
| lt   | <  Less than 小于 |
| le   | <=less equal    |
| gt   | > greater than  |
| ge   | >=greater equal |
| eq   | == equal        |
| ne   | != not equal    |

示例：compare.py

```python
class Tree:

def init(self, h):  # h 代表树干高度
    self.height = h

def show(self):
    # 画法此处省略了...
    print(" * ")
    print("***")
    print(" * ")
    print(" * ")

def lt(self, rhs):
    print("lt")
    return self.height < rhs.height

def le(self, rhs):
    print("le")
    return self.height <= rhs.height

def gt(self, rhs):
    return not (self <= rhs)

t1 = Tree(5)
t2 = Tree(10)
if t1 < t2:
    print("t2树高")
else:
    print("t1树高")

print(t1 <= t2)  # True
print(t1 > t2)
```

## 位运算符重载:

| 运算符    | 说明    |
| ------ | ----- |
| invert | ~ 取反  |
| and    | & 位与  |
| or     | \| 位或 |
| xor    | ^ 位异或 |
| lshift | << 左移 |
| rshift | >> 右移 |

## 内建函数的重载:

| 函数       | 说明            |
| -------- | ------------- |
| abs      | abs(obj)      |
| len      | len(obj)      |
| reversed | reversed(obj) |
| round    | round(obj)    |


示例：builtin_fn_overload.py
```python
class MyList:

    def init(self, a):
        self.data = a.copy()

    def str(self):
        return "MyList(" + str(self.data) + ")"

    def abs(self):
        temp = self.data.copy()
        for i in range(len(temp)):
            if temp[i] < 0:
                temp[i] = -temp[i]
        return MyList(temp)

L1 = MyList([1, -2, 3, -4])
L2 = abs(L1)  # MyList([1, 2, 3, 4])
print(L2)
```

示如:
```python
s1 = OrderSet([1,2,3,4])
s2 = OrderSet([3,4,5])

print(s1 & s2) # OrderSet({3,4})
print(s1 | s2) # OrderSet({1,2,3,4,5})
print(s1 ^ s2) # OrderSet({1,2,5})

if OrderSet([1,2,3]) != OrderSet([1,2,3,4]):
    print("不相等")
    ...
```

## 数值转换函数重载:

| 转换函数       | 说明      |
| ---------- | ------- |
| str(obj)   | str     |
| complex(x) | complex |
| int(obj)   | int     |
| float(obj) | float   |
| bool       | bool    |

例:
```python
  f = 3.14
  i = int(f)  # i = 3
```
示例见: int.py
```python
class MyNumber:

    def init(self, n):
        self.data = n

    def float(self):
        print("float被调用")
        try:
            x = float(self.data)
        except:
            x = 0.0
            if type(self.data) == complex:
                print('不能转换复数到浮点！返回默认值0.0')
        return x
        
n = MyNumber('100')
print(float(n))
n = MyNumber(1+2j)
print(float(n))
#print(float(1+2j))  # 出错
```
## bool测试运算符重载:

- 方法格式:  
```python
def bool(self):
      ....
```
- 作用:

  用于if 语句 的真值表达式中:
  用于while语句的真值表达式中:
  用于bool(obj) 函数取值

- 说明:

当没有bool(self)方法时，真值测试将以len(self)的方法的返回值来进行测试布尔值

示例见:bool.py

```python
class MyList:

    def init(self, count=0, value=0):
        self.data = []
        for x in range(count):
            self.data.append(value)

    def repr(self):
        return "MyList(" + repr(self.data) + ")"

    def len(self):
        return len(self.data)

    def bool(self):
        print("bool被调用")
        for x in self.data:
            if x:
                return True
        return False

myl = MyList(10, 0)
print(myl)  # MyList([0, 0, 0, 0.....])

if myl:
    print("MyList为真值")
else:
    print("MyList为假值")
```


## in / not in 运算符重载

- 重载方法:
```Python
def contains(self, e):
    pass
```
- 示例见： in_even.py
```Python
class even:

"偶数类,用于表示偶数的有序列表"

def init(self, begin, end):
    self.begin = begin
    self.end = end  # 不包含end

def contains(self, e):
    # print("contains被调用　．．．")
    if e < self.begin:
        return False
    if e >= self.end:
        return False
    if e % 2 == 0:
        return True
    return False

e1 = even(1, 10)

if 4 in e1:
    print("4在 even(1, 10) 中")
if 50 not in even(10, 20):
    print("50 不在列表:even(10, 20)")
    
print(50 in even(10, 20)) # False

if 3 in e1:
    print("3在 even(1, 10) 中")
else:
    print("3不在 even(1, 10) 中")
```

## 索引和切片运算符的重载:

- 重载方法：

| 重载方法                    | 说明        |
| ----------------------- | --------- |
| getitem(self, i)        | 用索引/切片获取值 |
| setitem(self, i, value) | 设置索引或切片的值 |
| delitem(self, i)        | 进行删除索引操作  |

- 作用：让自定义的对象能进行索引和切片操作

示意：
```python
L = [1,2,3,4]
L[2] = 3.14　　#  setitem
print(L[2])  #  getitem
del L[2]   # 删除索引  delitem
```
示例：index_slice.py

```Python
class MyList:

    def init(self, count=0, value=0):
        self.data = []
        for x in range(count):
            self.data.append(value)

    def repr(self):
        return "MyList(" + repr(self.data) + ")"

    def setValueAt(self, index, value):
        self.data[index] = value

    def setitem(self, index, value):
        self.data[index] = value

    def getitem(self, index):
        print("getitem被调用,index的值:", index)
        return self.data[index]

    def delitem(self, index):
        if index >= len(self.data):
            raise IndexError("%d在不允许的范围内" % index)
        if index < -len(self.data):
            raise IndexError("%d在不允许的范围内" % index)

        del self.data[index]
        # 以下示意不允许用del 进行索引操作
      # print("delitem被调用,index:", index)
      # print("del 啥也不做!!!")
        # raise TypeError

myl = MyList(5, 1)  # MyList([1, 1, 1, 1, 1])
myl[1] = 2		#myl[0::]=2  ???
print(myl[0::])

# myl.setValueAt(1, 2)  # MyList([1, 2, 1, 1, 1])
print(myl)
del myl[3]
print(myl)
```

## 函数调用(模拟)重载

- call 方法:
  - 作用:让一个对象能像函数一样被调用
  - 方法格式:

```python
def call(self, 参数列表):
      执行代码
```
注:此重载方法的参数可以是1个或多个形参

示意:
```python
class A:
   pass
      
 a = A()  # 创建对象
 a()  # ???? a能被调用吗?
```

示例：call.py

```Python
class MySum:

    def init(self):
        self.data = 0

    # def call(self, a, b):
    # def call(self):
    def call(self, *args, **kwargs):

  """函数调用方法重载"""

        print("args", args,  "kwargs:", kwargs)
        # print("call被调用...")
        s = sum(args)
        self.data += s
        return s
ms = MySum()
r = ms(100, 200)
print("r =", r)  # 300

r = ms(300, 400)
print("r =", r)  # 700

print("以前所有的数之和为:", ms.data)
```


## 属性管理重载:

- 四个属性管理的函数:

  - hasattr(obj, name[, default])
  - getattr(obj, name)
  - setattr(obj, name, value)  # x.y = 100
  - delattr(obj, name)

- 作用:

  1. 实现对特殊属性的管理
  2. 模拟一些特殊属性

- 重载格式:

  - def setattr(self, n, v):  设置属性      ....
  - def getattribute(self, n):  获取属性
  - def getattr(self, n):  在getattribute产生AttibuteError异常时重新偿试获取属性
  - def delattr(self, n):  删除属性

注:以上四个方法当属性不存在时,需要产生AttributeError异常错误

- 说明:
 - getattr在是找不到对应属性时才调用,当没有属性时需要产生AttributeError错误
 - getattribute 在任何时候都会被调用.当没有属性时需要产生AttributeError错误,然后进入getattr继续寻找

示例：attribute01.py

```Python
class Square:  # 正方形
#    length = 0

    def init(self, l):
        self.length = l  # 边长

    def setattr(self, name, value):
        print("setattr被调用!",self)
        if name == "perimeter":
           # self.length = value / 4
            self.dict['length'] = value /4
            self.dict['perimeter'] = value
        elif name == "length":
           # self.setattr(name,value)
            self.dict['length'] = value
            self.dict['perimeter'] = value*4

    def getattribute(self, name):  # 最先调用
        print("getattribute被调用")
        print('name=',name)
        return object.getattribute(self, name)
        #raise AttributeError

    def getattr(self, name):
        print("getattr被调用!")
        if name == 'area':
            return self.length**2
        '''
        if name == "perimeter":
            return self.length * 4
        elif name == "length":
            return self.length
        '''

    def delattr(self, name):
        if name == "perimeter":
            print("对不起不允许删除")
        raise AttributeError

sq = Square(10)
print(sq.length)
sq.pertimeter = 400
print(sq.area)
```
示例：attribute02.py

```Python
class Square:  # 正方形
    length = 0
    def init(self, l):
        self.class.length = l  # 边长
    def setattr(self, name, value):
      print("setattr被调用!")
        if name == "perimeter":
            self.class.length = value / 4
        elif name == "length":
            self.class.length = value

    def getattribute(self, name):  # 最先调用
        print("getattribute被调用")
      print('name=',name)
        #if name == "length":
        #    return self.class.length
        #raise AttributeError
        return object.getattribute(self,name)

    def getattr(self, name):
        print("getattr被调用!")
        if name == "perimeter":
            return self.class.length * 4
        elif name == "area":
            return self.class.length**2

    def delattr(self, name):
        if name == "perimeter":
            print("对不起不允许删除")
        raise AttributeError

sq = Square(10)
#sq.class.length
print(sq.length)  # 读取属性
sq.perimeter = 400  # 边长为100
print(sq.length)  # 读取属性
```