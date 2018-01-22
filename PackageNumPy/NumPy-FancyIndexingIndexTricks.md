布尔索引和花式索引

布尔索引
	使用布尔数组作为索引
	arr[condition]，condition为一个条件/多个条件组成的布尔数组。
	
>>> x = np.array([3,2,3,1,3,0])
# 布尔型数组的长度必须跟被索引的轴长度一致
>>> y = np.array([True,False,True,False,True,False]) 
>>> x[y]
array([3, 3, 3])
>>> x[y==False]
array([2, 1, 0])
>>> x>=3
array([ True, False,  True, False,  True, False], dtype=bool)
>>> x[~(x>=3)]
array([2, 1, 0])
>>> (x==2)|(x==1)
array([False,  True, False,  True, False, False], dtype=bool)
>>> x[(x==2)|(x==1)]
array([2, 1])
>>> x[(x==2)|(x==1)] = 0
>>> x  
[3 0 3 0 3 0]
	
花式索引
	使用整数数组作为索引
	
>>> x = np.array([1,2,3,4,5,6])
>>> x[[0,1,2]] 
array([1 2 3])
>>> x[[-1,-2,-3]] 
array([6,5,4])
>>> x = np.array([[1,2],[3,4],[5,6]])
>>> x[[0,1]] 
array([[1, 2],
       [3, 4]])
>>> x[[0,1],[0,1]]   #打印x[0][0]和x[1][1]
array([1, 4]) 			
>>> x[[0,1]][:,[0,1]] # 打印0,1行的0,1列 
array([[1, 2],
       [3, 4]])
>>> # 使用numpy.ix_()函数增强可读性
>>> x[np.ix_([0,1],[0,1])] #同上 打印01行的01列 
array([[1, 2],
       [3, 4]])
>>> x[[0,1],[0,1]] = [0,0]
>>> x 
array([[0, 2],
       [3, 0],
       [5, 6]])
	
使用字符串索引

要使用字符串作为索引，先来理解一下结构化数组：
Numpy提供强大的功能来创建结构化数据类型的数组。这些数组允许通过命名字段来操纵数据。一个简单的例子将演示它是什么意思：

x = np.array([('zhangsan',20,100),('lisi',20,90)],dtype=[('name','S10'),('age','i4'),('score','i4')])
>>> x
array([(b'zhangsan', 20, 100), (b'lisi', 20,  90)],
      dtype=[('name', 'S10'), ('age', '<i4'), ('score', '<i4')])
>>> x['name']
array([b'zhangsan', b'lisi'],
      dtype='|S10')
>>> x['score']
array([100,  90], dtype=int32)

上面例子中创建的array元素类型，看上去跟c语言中的结构体类型一样，通过dtype参数，可以传递结构体中每个属性列的命名和类型定义。
