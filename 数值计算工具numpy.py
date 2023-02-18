import numpy as np

a = np.array([2, 3, 4, 20, 16, 30])
b = np.array(((1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (10, 9, 1, 2, 3), (4, 5, 6, 7, 8)))
print("一维数组：", a)
print("二维数组：\n", b)

x = np.linspace(1, 10, 5)
print(x)
del x

x = np.linspace(1, 10, 100)  # 第三位为产生数据的个数
print(x)
del x

np.random.seed(0)  # 种子相同时，无论何时下面生成的随机数序列相同（不是随机数相同）
print([np.random.rand() for i in range(3)])

ar = np.array([i for i in range(100) if i % 2])
ar = ar.reshape(2,5,5)
print(ar)
print('\n')

ar = np.tile(ar, (2,1)) # 每个元素重复两次
print(ar)

A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print(A @ B)
print(A.dot(B))

b = np.arange(12).reshape(3,4)
print(b)
print('\n')
print(b.sum(axis=0))  # 每列的求和
print(b.sum(axis=1))  # 每行的求和
#  axis控制的实际上是维度，对于二维数据来说，0和1分别对应数据的列和行
print(b.cumsum(axis=1))  # 每行的前缀和
print(b.cumsum(axis=0))  # 每列的前缀和


b = np.arange(24,0,-1).reshape(2,3,4)
print(b)
b = b.T
print(b)

#  一维数组的T属性与原数组相同
a = np.arange(1,5)
print(a)
print(a.T)
print(a == a.T)

x = np.arange(12).reshape(3,4)
print(x)
print('\n')
print(x[0:2,0:2])  # 先取两行再取两列
print('\n')
print(x[0:2][0:2])  # 与上面不同##################???????/

a = np.array([[1,1,1],[1,1,1]])
b = np.array([2,2,2])
c = np.array([3,3,3])
print(np.vstack((a,b,c)))

x=np.array([[1],[2],[3]])
y=np.array([[4],[5],[6]])
# x=[[1],[2],[3]]
# y=[[4],[5],[6]]
print(np.hstack((x,y)))