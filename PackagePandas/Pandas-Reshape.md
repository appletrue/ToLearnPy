# 重塑Reshape

详情请查看 Hierarchical Indexing 和 [Reshaping](http://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-stacking)

## 使用stack()方法为DataFrame增加column

```python
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                         'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two',
                         'one', 'two', 'one', 'two']]))
``` 
-------------------插入zip()内置函数用法------------------------       
- 描述
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
- zip 语法：zip([iterable, ...])   # iterabl -- 一个或多个迭代器;
- 返回值:返回元组列表。
- 示例：
```python
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表.   [(1, 4), (2, 5), (3, 6)]
print(zip(a,c))       # 元素个数与最短的列表一致.   [(1, 4), (2, 5), (3, 6)]
print(zip(*zipped))   # 与 zip 相反，可理解为解压，返回二维矩阵式.   [(1, 2, 3), (4, 5, 6)]
```
------------------zip()----------------------------------------

```python
print(tuples)
#输出结果：
    [('bar', 'one'), ('bar', 'two'),
     ('baz', 'one'), ('baz', 'two'),
     ('foo', 'one'), ('foo', 'two'),
     ('qux', 'one'), ('qux', 'two')]
#pd.MultiIndex.from_tuples 将包含多个list的元组转换为复杂索引
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
```
-----------------help(pd.MultiIndex.from_tuples)-----------------------    
Help on method from_tuples in module pandas.core.indexes.multi:
参数： tuples : list / sequence of tuple-likes
例子：
```python
tuples = [(1, u'red'), (1, u'blue'),
          (2, u'red'), (2, u'blue')]
f = MultiIndex.from_tuples(tuples, names=('number', 'color'))
print(f)
#输出结果：
MultiIndex(levels=[[1, 2], ['blue', 'red']],
           labels=[[0, 0, 1, 1], [1, 0, 1, 0]],
           names=['number', 'color'])
```
--------------------pd.MultiIndex.from_tuples---------------------------
```python
print(index)
#输出结果：
    MultiIndex(levels=[[u'bar', u'baz', u'foo', u'qux'], [u'one', u'two']],
               labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
               names=[u'first', u'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print(df)
#输出结果：
                         A         B
    first second
    bar   one    -0.922059 -0.918091
          two    -0.825565 -0.880527
    baz   one     0.241927  1.130320
          two    -0.261823  2.463877
    foo   one    -0.220328 -0.519477
          two    -1.028038 -0.543191
    qux   one     0.315674  0.558686
          two     0.422296  0.241212
df2 = df[:4]
print(df2)
#输出结果：

                             A         B
    first second
    bar   one    -0.922059 -0.918091
          two    -0.825565 -0.880527
    baz   one     0.241927  1.130320
          two    -0.261823  2.463877

#以下应用stack()
stacked = df2.stack()    #??明明增加行啊。。。
print(stacked)
#输出结果：
    first  second
    bar    one     A   -0.922059
                   B   -0.918091
           two     A   -0.825565
                   B   -0.880527
    baz    one     A    0.241927
                   B    1.130320
           two     A   -0.261823
                   B    2.463877
    dtype: float64

print(stacked.unstack())     #使用unstack()方法还原stack的DataFrame，默认还原最后一级，也可以自由指定

#输出结果：
                     A         B
                     A         B
    first second
    bar   one    -0.922059 -0.918091
          two    -0.825565 -0.880527
    baz   one     0.241927  1.130320
          two    -0.261823  2.463877
          
print(stacked.unstack(1))
    second        one       two
    first
    bar   A -0.922059 -0.825565
          B -0.918091 -0.880527
    baz   A  0.241927 -0.261823
          B  1.130320  2.463877
          
print(stacked.unstack(0))
    first          bar       baz
    second
    one    A -0.922059  0.241927
           B -0.918091  1.130320
    two    A -0.825565 -0.261823
           B -0.880527  2.463877
``` 

## 透视表——理解为自由组合表的行与列，类似于交叉报表（Excel中透视表）

详情请查看 [Pivot Tables](http://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-pivot)

示例:
```python
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
                   
#构造透视表:  
#按照A，B两列作为项目，汇总C 列对应的D 列的值。
p1 = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
print(p1)
#输出结果：
    C             bar       foo
    A     B
    one   A -1.250611 -1.047274
          B  1.532134 -0.455948
          C  0.125989 -0.500260
    three A  0.623716       NaN
          B       NaN  0.095117
          C -0.348707       NaN
    two   A       NaN  0.390363
          B -0.743466       NaN
          C       NaN  0.792279
```
