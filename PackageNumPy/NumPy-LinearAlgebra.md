线性代数

继续工作。这里包括基本线性代数。


简单数组操作

有关更多信息，请参阅numpy目录中的linalg.py。


>>> import numpy as np
>>> a = np.array([[1.0, 2.0], [3.0, 4.0]])
>>> print(a)
[[ 1.  2.]
 [ 3.  4.]]

>>> a.transpose()
array([[ 1.,  3.],
       [ 2.,  4.]])

>>> np.linalg.inv(a)
array([[-2. ,  1. ],
       [ 1.5, -0.5]])

>>> u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
>>> u
array([[ 1.,  0.],
       [ 0.,  1.]])
>>> j = np.array([[0.0, -1.0], [1.0, 0.0]])

>>> np.dot (j, j) # matrix product
array([[-1.,  0.],
       [ 0., -1.]])

>>> np.trace(u)  # trace
2.0

>>> y = np.array([[5.], [7.]])
>>> np.linalg.solve(a, y)
array([[-3.],
       [ 4.]])

>>> np.linalg.eig(j)
(array([ 0.+1.j,  0.-1.j]), array([[ 0.70710678+0.j        ,  0.70710678-0.j        ],
       [ 0.00000000-0.70710678j,  0.00000000+0.70710678j]]))

-------------------------------------------
线性代数（numpy.linalg）


矩阵和向量积

dot（a，b [，out]） 两个数组的点积。 
vdot（a，b） 返回两个向量的点积。 
inner（a，b） 两个数组的内积。 
outer（a，b [，out]） 计算两个向量的外积。 
matmul（a，b [，out]） 两个数组的矩阵乘积。 
tensordot（a，b [，axes]） 对于数组> = 1-D，沿指定轴计算张量点积。 
einsum（下标，\ * operands [，out，dtype，...]） 评估操作数上的爱因斯坦求和约定。 
linalg.matrix_power（M，n） 将方阵转化为（整数）幂n。 
kron（a，b） 克罗内克两个数组的乘积。 

分解
Decompositions

linalg.cholesky（a） Cholesky分解。 
linalg.qr（a [，mode]） 计算矩阵的qr因式分解。 
linalg.svd（a [，full_matrices，compute_uv]） 奇异值分解。 


矩阵特征值

linalg.eig(a) 计算正方形数组的特征值和右特征向量。 
linalg.eigh(a[, UPLO]) 返回Hermitian或对称矩阵的特征值和特征向量。 
linalg.eigvals(a) 计算一般矩阵的特征值。 
linalg.eigvalsh(a[, UPLO]) 计算Hermitian或真实对称矩阵的特征值。 

范数和其他数字
Norms and other numbers

linalg.norm（x [，ord，axis，keepdims]） 矩阵或向量范数。 
linalg.cond（x [，p]） 计算矩阵的条件数。 
linalg.det（a） 计算数组的行列式。 
linalg.matrix_rank（M [，tol]） 使用SVD方法返回数组的矩阵秩 
linalg.slogdet（a） 计算数组的行列式的符号和（自然）对数。 
trace（a [，offset，axis1，axis2，dtype，out]） 沿数组的对角线返回总和。 

求解方程和求逆矩阵
Solving equations and inverting matrices

linalg.solve（a，b） 求解线性矩阵方程或线性标量方程组。 
linalg.tensorsolve（a，b [，axes]） 为x解出张量方程a x = b 
linalg.lstsq（a，b [，rcond]） 将最小二乘解返回到线性矩阵方程。 
linalg.inv（a） 计算矩阵的（乘法）逆。 
linalg.pinv（a [，rcond]） 计算矩阵的（Moore-Penrose）伪逆。 
linalg.tensorinv（a [，ind]） 计算N维数组的“逆”。 

异常
Exceptions

linalg.LinAlgError linalg函数引发的通用Python异常派生对象。 
