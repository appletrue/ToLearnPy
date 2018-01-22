	- range（）函数
	- 循环语句：
	  - while
	  - for
	  - break
	  - continue
	  - 死循环

======================================================

### range()函数
```python
>>> help(range)
#输出如下：
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop
```
- range(stop) :从零开始，每次生成一个整数，后加1操作，直到stop为止(不包含stop)
- range(start, stop[, step])
  — start 开始<br>
  — stop  结束(不包含stop)<br>
  — step  步长(可以为负数,且可以省略)<br>

例：
```python
range(3)        # 0, 1, 2
  range(5)        # 0, 1, 2, 3, 4
  range(1, 3)     # 1, 2
  range(1, 8, 2)  # 1, 3, 5, 7
  range(5, 0, -1) # 5, 4, 3, 2, 1
  range(5, 0, -2) # 5, 3, 1
  range(4, 0)     #空,啥也没有
for x in range(10):
   print(x)
```
python3 种已没有 xrange（）函数，被 range（） 代替。    
xrange():
是一种range的优化。<br>
a=range(10)<br>
a:[0,1,2,3,4,5,6,7,8,9]<br>
type(a): list  返回是list类型，适合需要list的情况

a=xrange(10)<br>
a:xrange(10)<br>
type(a):xrange 返回是生成器，不占大内存，更优化，适合不需要返回值的情况