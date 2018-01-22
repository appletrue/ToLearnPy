# Pandas 运算

### 统计(操作通常情况下不包含缺失项)

1.按列求平均值:

```python
print(df.mean()） #执行(axis=0)描述性统计
A   -0.620884
B    0.128655
C   -0.198127
D    5.000000
F    3.000000
dtype: float64
```

2.按行求平均值:

```python
print(df.mean(1))       #执行列（axis=1）描述统计
2013-01-01    1.253112
2013-01-02    1.208060
2013-01-03    1.303966
2013-01-04    1.456889
2013-01-05    1.462384
2013-01-06    1.737785
Freq: D, dtype: float64
```

3.操作不同的维度需要先对齐,pandas会沿着指定维度执行:

```python
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
print(s)
2013-01-01   NaN
2013-01-02   NaN
2013-01-03     1
2013-01-04     3
2013-01-05     5
2013-01-06   NaN
Freq: D, dtype: float64
print(df.sub(s, axis='index'))
               A         B         C   D   F
2013-01-01       NaN       NaN       NaN NaN NaN
2013-01-02       NaN       NaN       NaN NaN NaN
2013-01-03 -1.719234 -1.396174 -0.364763   4   1
2013-01-04 -3.921692 -2.123307 -3.670553   2   0
2013-01-05 -5.300317 -5.011320 -6.376442   0  -1
2013-01-06       NaN       NaN       NaN NaN NaN
```
注:

这里对齐维度指的对齐时间index
shift(2)指沿着时间轴将数据顺移两位
sub指减法，与NaN进行操作，结果也是NaN

### apply 应用:用apply方法将函数用于数据

1.apply function:

```python
print(df.apply(np.cumsum))
                       A         B         C   D   F
    2013-01-01  0.000000  0.000000  0.012447   5 NaN
    2013-01-02  0.119622 -0.484051  0.417175  10   1
    2013-01-03 -0.599612 -0.880225  1.052412  15   3
    2013-01-04 -1.521304 -0.003532  0.381859  20   6
    2013-01-05 -1.821621 -0.014853 -0.994583  25  10
    2013-01-06 -3.725304  0.771932 -1.188763  30  15

print(df.apply(lambda x: x.max() - x.min()))
    A    2.023304
    B    1.360744
    C    2.011679
    D    0.000000
    F    4.000000
    dtype: float64
注: - cumsum 累加

详情请查看 直方图和离散化

### 直方图:
```python
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
    0    1
    1    3
    2    5
    3    1
    4    6
    5    1
    6    3
    7    4
    8    0
    9    3
    dtype: int64
print(s.value_counts())
    3    3
    1    3
    6    1
    5    1
    4    1
    0    1
    dtype: int64
```

pandas默认配置了一些字符串处理方法，可以方便的操作元素，如下所示:(详情请查看 Vectorized String Methods)

### 字符串方法:

```python
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())
    0       a
    1       b
    2       c
    3    aaba
    4    baca
    5     NaN
    6    caba
    7     dog
    8     cat
    dtype: object
```
