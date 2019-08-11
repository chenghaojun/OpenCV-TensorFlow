import numpy as np

data1 = np.array([1, 2, 3, 4, 5, 6])
print(data1)

data2 = np.array([
    [1, 2],
    [3, 4]
])
print(data2)

# 打印维度
print(data1.shape, data2.shape)

# 空矩阵和单位矩阵
print(np.zeros([2, 3]))
print(np.ones([2, 2]))


# 矩阵的修改和查询
data2[1, 0] = 5  # 不能当数组来看待的。[1][0] 的取值方式不对
print('修改矩阵：%s' % data2)
print('矩阵取值：%s' % data2[1,0])  # 把 5 取出来
assert data2[1,0] == 5

# 矩阵乘法
# 数乘
data3 = np.ones([2, 3])
print(data3 * 2)
print(data3 / 2)
print(data3 + 4)

data4 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("矩阵乘法", (data3 * 2) * data4)

