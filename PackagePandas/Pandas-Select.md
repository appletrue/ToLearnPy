## 选择数据

虽然标准的Python/Numpy表达式是直观且可用的，但是我们推荐使用优化后的pandas方法,例如:.at,.iat,.loc,.iloc以及.ix 

详情请查看: Indexing and Selecting Data 和 MultiIndex / Advanced Indexing

### 获取

1. 选择一列，返回Series，相当于df.A:

```python
import pandas as pd
import numpy as np

df = pd.pivot_table(t, values='D', index=['A', 'B'], columns=['C'])
print(df['A']）
2013-01-01    0.938663
2013-01-02   -0.984496
2013-01-03    1.380548
2013-01-04   -1.435851
2013-01-05    1.269714
2013-01-06   -0.112897
Freq: D, Name: A, dtype: float64
```

2.通过[]选择，即对行进行切片:

```python
print(df[0:3])
                   A         B         C         D
2013-01-01  1.255612  0.324482 -0.449985  0.730572
2013-01-02 -0.180358  0.045876 -0.295605  0.164941
2013-01-03 -0.424212 -0.067818  1.392858  1.430352
```
### 标签式选择

1.通过标签获取交叉区域:

```python
print(df.loc[dates[0]])     #注:即获取时间为2013-01-01的数据
A   -0.415671
B   -1.531572
C    0.281520
D    0.413375
Name: 2013-01-01 00:00:00, dtype: float64


2.通过标签获取多轴数据:

```python
df.loc[:,['A','B']]
                      A         B
    2013-01-01  0.859619 -0.545903
    2013-01-02  0.119622 -0.484051
    2013-01-03 -0.719234 -0.396174
    2013-01-04 -0.921692  0.876693
    2013-01-05 -0.300317 -0.011320
    2013-01-06 -1.903683  0.786785
```

3.标签切片:

```python
df.loc['20130102':'20130104',['A','B']]
                       A         B
    2013-01-02  0.119622 -0.484051
    2013-01-03 -0.719234 -0.396174
    2013-01-04 -0.921692  0.876693
```

4.对返回的对象缩减维度:

```python
df.loc['20130102',['A','B']]
    A    0.119622
    B   -0.484051
    Name: 2013-01-02 00:00:00, dtype: float64
```

5.获取单个值:

```python
print(df.loc[dates[0],'A'])     #    0.85961861159875042
```

6.快速访问单个标量（同5）:

```python
print(df.at[dates[0],'A'])      # 0.85961861159875042
```

注:loc通过行标签获取行数据，iloc通过行号获取行数据

## 位置式选择

1.通过数值选择:

```python
print(df.iloc[3])
A   -0.921692
B    0.876693
C   -0.670553
D    1.468060
Name: 2013-01-04 00:00:00, dtype: float64
```

2.通过数值切片:

```python
print(df.iloc[3:5,0:2])
               A         B
2013-01-04 -0.921692  0.876693
2013-01-05 -0.300317 -0.011320
 ```
注:左开右闭

3.通过指定列表位置:

```python
print(df.iloc[[1,2,4],[0,2]])
                   A         C
2013-01-02  0.119622  0.404728
2013-01-03 -0.719234  0.635237
2013-01-05 -0.300317 -1.376442
```

4.对行切片:

```python
print(df.iloc[1:3,:])
                   A         B         C         D
2013-01-02  0.119622 -0.484051  0.404728  0.360880
2013-01-03 -0.719234 -0.396174  0.635237  0.216691
```
5.对列切片:显示切片列

```python
print(df.iloc[:,1:3])
               B         C
2013-01-01 -0.545903  0.012447
2013-01-02 -0.484051  0.404728
2013-01-03 -0.396174  0.635237
2013-01-04  0.876693 -0.670553
2013-01-05 -0.011320 -1.376442
2013-01-06  0.786785 -0.194179
```

6.获取特定值:

```python
print(df.iloc[1,1])         #    -0.48405080229207309
```

7.快速访问某个标量（同6）:

```python
print(df.iat[1,1])          #    -0.48405080229207309
```

### Boolean索引

1.通过某列选择数据:

```python
print(df[df.A > 0])
                   A         B         C         D
2013-01-01  0.859619 -0.545903  0.012447  1.257684
2013-01-02  0.119622 -0.484051  0.404728  0.360880
```

2.通过where方法选择数据:

```python
print(df[df > 0])
               A         B         C         D
2013-01-01  0.859619       NaN  0.012447  1.257684
2013-01-02  0.119622       NaN  0.404728  0.360880
2013-01-03       NaN       NaN  0.635237  0.216691
2013-01-04       NaN  0.876693       NaN  1.468060
2013-01-05       NaN       NaN       NaN  1.694740
2013-01-06       NaN  0.786785       NaN  0.177973
```

3.通过** isin()** 过滤数据:

```python
print(df2 = df.copy())
print(df2['E'] = ['one', 'one','two','three','four','three'])
print(df2)
                   A         B         C         D      E
2013-01-01  0.859619 -0.545903  0.012447  1.257684    one
2013-01-02  0.119622 -0.484051  0.404728  0.360880    one
2013-01-03 -0.719234 -0.396174  0.635237  0.216691    two
2013-01-04 -0.921692  0.876693 -0.670553  1.468060  three
2013-01-05 -0.300317 -0.011320 -1.376442  1.694740   four
2013-01-06 -1.903683  0.786785 -0.194179  0.177973  three

print(df2[df2['E'].isin(['two','four'])])
                   A         B         C         D     E
2013-01-03 -0.719234 -0.396174  0.635237  0.216691   two
2013-01-05 -0.300317 -0.011320 -1.376442  1.694740  four
```
    
设置

1.新增一列数据:设置新列会自动按索引对齐数据。

```python
print(s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))）
print(s1)
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
df['F'] = s1
```

2.通过标签更新值:

```python
df.at[dates[0],'A'] = 0
```

3.通过位置更新值:

```python
df.iat[0,1] = 0     
```

4.通过分配numpy数组更新一列值:

```python
df.loc[:,'D'] = np.array([5] * len(df)) 
```

上面几步操作的结果:

```python
print(df)
                   A         B         C  D   F
2013-01-01  0.000000  0.000000  0.012447  5 NaN
2013-01-02  0.119622 -0.484051  0.404728  5   1
2013-01-03 -0.719234 -0.396174  0.635237  5   2
2013-01-04 -0.921692  0.876693 -0.670553  5   3
2013-01-05 -0.300317 -0.011320 -1.376442  5   4
2013-01-06 -1.903683  0.786785 -0.194179  5   5
```

5.通过where更新值:

```python
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)
                   A         B         C  D   F
2013-01-01  0.000000  0.000000 -0.012447 -5 NaN
2013-01-02 -0.119622 -0.484051 -0.404728 -5  -1
2013-01-03 -0.719234 -0.396174 -0.635237 -5  -2
2013-01-04 -0.921692 -0.876693 -0.670553 -5  -3
2013-01-05 -0.300317 -0.011320 -1.376442 -5  -4
2013-01-06 -1.903683 -0.786785 -0.194179 -5  -5
```
