
## 统计函数

### 常规统计

```python
x = np.array([[1,2],[3,3],[1,2]])    #同一维度上的数组长度须一致
print(x.mean())                      #> > > 2.0
print(x.mean(axis=1))                # 对每一行的元素求平均
print(array([ 1.5,  3. ,  1.5]))
print(x.mean(axis=0))                # 对每一列的元素求平均
                                     #array([ 1.66666667,  2.33333333])
print(x.sum())                       #同理 , 12
print(x.sum(axis=1))                 #对每一行求和
print(array([3, 6, 3])
print(x.max()              #3
print(x.max(axis=1) 	      #求每一行最大值
                           #array([2, 3, 2])
print(x.cumsum() 			   #累积求和，默认是求扁平数组
                           # array([ 1,  3,  6,  9, 10, 12])
print(x.cumsum(axis=1)		#每一行累积求和
                           #array([[1, 3],
                                   [3, 6],
                                   [1, 3]])

print(x.cumprod())    		#累积求积，默认是求扁平数组
                           #array([ 1,  2,  6, 18, 18, 36])
print(x.cumprod(axis=1))	#每一行累积求积
                           #array([[1, 2],
                                   [3, 9],
                                   [1, 2]])
```

### 用于布尔数组的统计方法：

sum : 统计数组/数组某一维度中的True的个数

any： 统计数组/数组某一维度中是否存在一个/多个True

all：统计数组/数组某一维度中是否都是True

```python
x = np.array([[True,False],[True,False]])
print(x.sum())                 # 2
print(x.sum(axis=1))           #array([1, 1])
print(x.sum(axis=0))           #array([2, 0])
print(x.any(axis=0))           #array([ True, False], dtype=bool)
print(x.all(axis=1))           #array([False, False], dtype=bool)
```


### 去重和集合运算
```python
x = np.array([[1,6,2],[6,1,3],[1,5,2]])
print(np.unique(x)) 				#去重array([1, 2, 3, 5, 6])
y = np.array([1,6,5])
print(np.in1d(x,y)) 				#测试x每个元素是否存在于y
                              #array([ True,  True, False,  True,  True, False,  True,  True, False], dtype=bool)
print(np.setdiff1d(x,y)) 	   # 求差集array([2, 3])
print(np.intersect1d(x,y))    #	求交集array([1, 5, 6])		
print(np.union1d(x.ravel,y))	# 求并集,要求维度相同array([1, 2, 3, 5, 6])
print(np.setxor1d(y,x)) 		# 求集的异或，互差的并集array([2, 3])
```

### 统计函数：Counting

| 函数                | 说明         |
| ------------------ | ------------ |
|count_nonzero（a）| 计算数组a中非零值的数量|		

### 次序统计：Order statistics

| 函数                | 说明         |
| ------------------ | ------------ |
|amin（a [，axis，out，keepdims]）| 沿轴返回数组或最小值的最小值。 |
|amax（a [，axis，out，keepdims]） |返回沿轴的数组或最大值的最大值。 |
|nanmin（a [，axis，out，keepdims]） |沿轴返回数组或最小值，忽略任何NaN。 |
|nanmax（a [，axis，out，keepdims]） |返回沿轴的数组或最大值的最大值，忽略任何NaN。 |
|ptp（a [，axis，out]）| 沿轴的值范围（最大 - 最小）。 |
|percentile（a，q [，axis，out，...]） |沿指定轴计算数据的第q个百分位数。 |
|nanpercentile（a，q [，axis，out，...]） |沿着指定轴计算数据的第q个百分位数，而忽略nan值。 |

### 均值和方差：Averages and variances

| 函数                | 说明         |
| ------------------ | ------------ |
|median（a [，axis，out，overwrite_input，keepdims]）| 计算沿指定轴的中值。 |
|average（a [，axis，weights，returned]） |沿指定轴计算加权平均值。 |
|mean（a [，axis，dtype，out，keepdims]） |沿指定轴计算算术平均值。 |
|std（a [，axis，dtype，out，ddof，keepdims]） |计算沿指定轴的标准偏差。 |
|var（a [，axis，dtype，out，ddof，keepdims]） |计算沿指定轴的方差。 |
|nanmedian（a [，axis，out，overwrite_input，...]）| 沿着指定轴计算中值，而忽略NaN。 |
|nanmean（a [，axis，dtype，out，keepdims]） |沿着指定的轴计算算术平均值，忽略NaN。 |
|nanstd（a [，axis，dtype，out，ddof，keepdims]） |计算沿着指定轴的标准偏差，而忽略NaN。 |
|nanvar（a [，axis，dtype，out，ddof，keepdims]） |计算沿指定轴的方差，而忽略NaN。 |

### 相关：Correlating

| 函数                | 说明         |
| ------------------ | ------------ |
|corrcoef（x [，y，rowvar，bias，ddof]） |返回Pearson乘积矩相关系数。 |
|correlate（a，v [，mode]） |两个1维序列的互相关。 |
|cov（m [，y，rowvar，bias，ddof，fweights，...]） |估计协方差矩阵，给定数据和权重。 |

### 直方图：Histograms

| 函数                | 说明         |
| ------------------ | ------------ |
|histogram（a [，bins，range，normed，weights，...] |计算一组数据的直方图。 |
|histogram2d（x，y [，bins，range，normed，weights]） |计算两个数据样本的二维直方图。 |
|histogramdd（sample [，bins，range，normed，...]）| 计算一些数据的多维直方图。 |
|bincount（x [，weights，minlength]） |计算非负整数数组中每个值的出现次数。| 
|digitize（x，bins [，right]） |返回输入数组中每个值所属的bin的索引 |


## 随机数抽样

### 随机数生成

在构造矩阵时，利用随机数生成是常用的方法，在[Reference](https://docs.scipy.org/doc/numpy/reference/index.html)查表可以找到随机数生成的模块[函数清单](https://docs.scipy.org/doc/numpy/reference/routines.random.html)，根据说明选择自己需要的函数。

### np.random.randint：用来生成指定的整形随机数数组

```
x_arr = np.random.randint(-1,2,10)
y_arr = np.random.randint(-1,2,10)
coordinate = np.column_stack((x_arr,y_arr))
print(coordinate)
```

```python
import numpy.random as npr

x = npr.randint(0,2,size=100000)       #抛硬币
print( (x>0).sum())                    # 正面的结果,每次实验结果不一定相同
print(npr.normal(size=(2,2)))          #正态分布随机数数组 shape = (2,2)
#输出结果：
49794
[[ 0.26070424 -1.38225756]
 [-0.9534146  -0.17745009]]
```

函数库随机抽样（numpy.random）

### 简单的随机数据

| 函数                | 说明         |
| ------------------ | ------------ |
|rand(d0, d1, ..., dn) |以给定的形状返回随机值。 |
|randn(d0, d1, ..., dn) \从“标准正态”分布返回一个样本（或多个样本）。 |
|randint(low[, high, size, dtype]) |返回从low（包括）到high（不包括）的随机整数。 |
|random_integers(low[, high, size])\| low和high之间的np.int类型的随机整数（含）。 |
|random_sample([size]) 在半开间隔[0.0，1.0]中返回随机浮点数。 |
|random([size]) 在半开间隔[0.0，1.0]中返回随机浮点数。 |
|ranf([size]) 在半开间隔[0.0，1.0]中返回随机浮点数。 |
|sample([size]) |在半开间隔[0.0，1.0]中返回随机浮点数。| 
|choice(a[, size, replace, p]) |从给定的1-D数组生成随机样本 |
|bytes(length)| 返回随机字节。 |

### 排列

| 函数                | 说明         |
| ------------------ | ------------ |
|shuffle(x) |通过随机播放其内容来修改序列。 |
|permutation(x) |随机置换序列，或返回置换范围。 |

### 分布

| 函数                | 说明         |
| ------------------ | ------------ |
| beta（a，b [，size]）                        | 从Beta分布绘制样本   |
| binomial(n, p[, size])                   | 从二项分布绘制样本     |
| chisquare（df [，size]）                    | 从卡方分布绘制样本  |
| dirichlet（alpha [，size]）                 | 从Dirichlet分布绘制样本  |
| exponential（[scale，size]）                | 从指数分布绘制样本    |
| f（dfnum，dfden [，size]）                   | 从F分布绘制样本    |
| gamma（shape [，scale，size]）               | 从Gamma分布绘制样本   |
| geometric（p [，size]）                     | 从几何分布绘制样本  |
| gumbel（[loc，scale，size]）                 | 从Gumbel分布绘制样本  |
| hypergeometric(ngood, nbad, nsample[, size]) | 从超几何分布绘制样本  |
| laplace（[loc，scale，size]）                | 从拉普拉斯或指定位置（或平均值）和比例（衰减）的双指数分布绘制样本。 |
| logistic（[loc，scale，size]）               | 从逻辑分布绘制样本  |
| lognormal（[mean，sigma，size]）             | 从对数正态分布绘制样本  |
| logseries（p [，size]）                     | 从对数系列分布绘制样本   |
| multinomial（n，pvals [，size]）             | 从多项分布绘制样本  |
| multivariate_normal(mean, cov[, size])   | 从多变量正态分布绘制随机样本  |
| negative_binomial(n, p[, size])          | 从负二项分布绘制样本  |
| noncentral_chisquare（df，nonc [，size]）    | 从非中心卡方分布绘制样本   |
| noncentral_f(dfnum, dfden, nonc[, size]) | 从非中心F分布中抽取样本  |
| normal（[loc，scale，size]）                 | 从正态（高斯）分布绘制随机样本  |
| pareto（a [，size]）                        | 从具有指定形状的Pareto II或Lomax分布绘制样品   |
| poisson（[lam，size]）                      | 从泊松分布绘制样本   |
| power（a [，size]）                         | 从具有正指数a-1的功率分布中在[0，1]中绘制样本 |
| vrayleigh（[scale，size]）                  | 从瑞利分布绘制样本  |
|standard_cauchy（[size]）                   |从模式= 0的标准Cauchy分布绘制样本| 
|standard_exponential（[size]）             | 从标准指数分布绘制样本 |
|standard_gamma（shape [，size]）             |从标准Gamma分布绘制样本 |
|standard_normal（[size]）                  | 从标准正态分布绘制样品（平均值= 0，stdev = 1） |
|standard_t（df [，size] ）                  | 从具有df自由度的标准学生t分布绘制样本| 
|triangular（left，mode，right [，size]）    |从三角分布绘制样本 |
|uniform（[low，high，size]）              |从均匀分布绘制样本 |
|vonmises（mu，kappa [，size]）             |从von Mises分布绘制样本。 |
|wald（mean，scale [，size]）              |从Wald或反高斯分布绘制样本。 |
|weibull（a [，size]）                    |从威布尔分布绘制样本。| 
|zipf（a [，size]）                        |从Zipf分布绘制样本。 |

### 随机数生成器
| 函数                | 说明         |
| ------------------ | ------------ |
|RandomState Mersenne Twister |伪随机数生成器的容器。 |
|seed([seed])                 |种子发电机。 |
|get_state()                  |返回表示生成器的内部状态的元组。 |
|set_state(state)              |从元组中设置发生器的内部状态。 |
