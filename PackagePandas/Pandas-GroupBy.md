
 分组
group by: - Splitting 将数据分组 - Applying 对每个分组应用不同的function - Combining 使用某种数据结果展示结果 详情请查看 Grouping section

举个栗子:

>>> df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                       'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
                       'C' : np.random.randn(8),
                       'D' : np.random.randn(8)})
>>> df
         A      B         C         D
    0  foo    one -0.655020 -0.671592
    1  bar    one  0.846428  1.884603
    2  foo    two -2.280466  0.725070
    3  bar  three  1.166448 -0.208171
    4  foo    two -0.257124 -0.850319
    5  bar    two -0.654609  1.258091
    6  foo    one -1.624213 -0.383978
    7  foo  three -0.523944  0.114338
分组后sum求和:

>>> df.groupby('A').sum()
                C         D
    A
    bar  1.358267  2.934523
    foo -5.340766 -1.066481
对多列分组后sum:

>>> df.groupby(['A','B']).sum()
                      C         D
    A   B
    bar one    0.846428  1.884603
        three  1.166448 -0.208171
        two   -0.654609  1.258091
    foo one   -2.279233 -1.055570
        three -0.523944  0.114338
        two   -2.537589 -0.125249
