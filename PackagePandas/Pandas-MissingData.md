# 缺失数据处理

pandas用np.nan代表缺失数据，详情请查看 Missing Data section

### reindex()可以修改/增加/删除索引，会返回一个数据的副本:

```python
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
print(df1)
                       A         B         C  D   F   E
    2013-01-01  0.000000  0.000000  0.012447  5 NaN   1
    2013-01-02  0.119622 -0.484051  0.404728  5   1   1
    2013-01-03 -0.719234 -0.396174  0.635237  5   2 NaN
    2013-01-04 -0.921692  0.876693 -0.670553  5   3 NaN
```

### 丢掉含有缺失项的行:

```python
print(df1.dropna(how='any'))
                       A         B         C  D  F  E
    2013-01-02  0.119622 -0.484051  0.404728  5  1  1
```

### 对缺失项赋值:

```python
print(df1.fillna(value=5))
                       A         B         C  D  F  E
    2013-01-01  0.000000  0.000000  0.012447  5  5  1
    2013-01-02  0.119622 -0.484051  0.404728  5  1  1
    2013-01-03 -0.719234 -0.396174  0.635237  5  2  5
    2013-01-04 -0.921692  0.876693 -0.670553  5  3  5
```

### 对缺失项布尔赋值:

```python
print(pd.isnull(df1))
              A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
```
