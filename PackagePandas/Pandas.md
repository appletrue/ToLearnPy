- 数据集的读取或载入

× 方式一： ————读取本地下载文件————pkg：pandas
> import pandas   
iris = pandas.read_csv("iris.csv")    
print(iris.shape) # .shape获取row & column （150,4）    
print(iris.head(2)) # 获取前2行数据    
print(iris.describe()) # 对数据进行描述（体现numFive）

× 方式二：
————读取sklearn 包下内置数据集
> from sklearn.datasets import load_iris    
iris = load_iris() #读取本地pkg：sklearn 下内置数据集      
print(iris.feature_names) #输入变量特征值的名称（自变量）    
print(iris.target_names) # 输出变量即目标变量的名称（因变量）    
print(list(iris.target_names)) ## 该数据集是一种字典结构，数据存储在.data 成员中，输出标签存储在 .target成员中    
print(iris.data[0]) #首行数据    
print(iris.target[0])

或者以下实现方式：
> from sklearn import datasets    
iris = datasets.load_iris()    
irisFeatures = iris["data"]    
irisFeaturesName = iris["feature_names"]    
irisLabels = iris["target"]    
print(irisFeatures) # 打印输入值     
print(irisLabels) # 打印输出值     
print(irisFeaturesName) #打印特征值的名称    
print(datasets.groupby('class').size())     

× 方式三：
————从网址下载读取 Load datasets
> import pandas    
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"    
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']    
dataset = pandas.read_csv(url) #读取csv数据    
print(dataset.shape) # .shape获取row & column （149,5）    
print(dataset.head(3)) # 获取前3行数据    
----结果-----：
5.1 3.5 1.4 0.2 Iris-setosa
0 4.9 3.0 1.4 0.2 Iris-setosa
1 4.7 3.2 1.3 0.2 Iris-setosa
2 4.6 3.1 1.5 0.2 Iris-setosa
