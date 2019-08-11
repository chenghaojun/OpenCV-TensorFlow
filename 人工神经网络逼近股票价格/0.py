import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

date = np.linspace(1, 15, 15)  # 定义一个 15 个元素的数组
endPrice = np.array([
    2511.90,2538.26,2510.68,2591.66,2732.98,2701.69,2701.29,2678.67,2726.50,2681.50,2739.17,2715.07,2823.58,2864.90,2919.08
])
beginPrice = np.array([
    2438.71,2500.88,2534.95,2512.52,2594.04,2743.26,2697.47,2695.24,2678.23,2722.13,2674.93,2744.13,2717.46,2832.73,2877.40
])

for i in range(0, 15):
    # 1. 绘制柱状图
    dateOne = np.zeros([2])
    dateOne[0] = i
    dateOne[1] = i
    priceOne = np.zeros([2])
    priceOne[0] = beginPrice[i]
    priceOne[1] = endPrice[i]

    if endPrice[i] > beginPrice[i]:
        plt.plot(dateOne, priceOne, 'r', lw = 10)
    else:
        plt.plot(dateOne, priceOne, 'g', lw = 10)

# A：输入层
# B：中间层
# C：隐藏层
# 通过输入某一个天数得到当天的股票价格
# A(15*1) * w1(1*10) + b1(1*10) = B(15*10)
# B(15*10) * w2(10*1) + b2(15*1) = C(15*1)

# 输入层 归一化
dateNormal = np.zeros([15,1])
priceNormal = np.zeros([15,1])
for i in range(0, 15):
    dateNormal[i, 0] = i / 14.0
    priceNormal[i, 0] = beginPrice[i] / 3000.0
x = tf.placeholder(tf.float32, [None, 1]) # 表明是 N 行一列的
y = tf.placeholder(tf.float32, [None, 1]) # 表明是 N 行一列的

# 隐藏层，和 w1\w2, b1\b2 相关
w1 = tf.Variable(tf.random_uniform([1, 10], 0, 1))  # 0, 1 表示的是取值范围，这也是之前为什么要做归一化
b1 = tf.Variable(tf.zeros([1, 10]))

wb1 = tf.matmul(x, w1) + b1
layer1 = tf.nn.relu(wb1)  # 激励函数


# 输出层
w2 = tf.Variable(tf.random_uniform([10, 1], 0, 1))
b2 = tf.Variable(tf.zeros([15, 1]))

wb2 = tf.matmul(layer1, w2) + b2
layer2 = tf.nn.relu(wb2)

loss = tf.reduce_mean(tf.square(y-layer2))  # y 真实值 layer2 计算，其实就是个标准差
tranStep = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # 每次下降 0.1 ，获取更小的 loss 值

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(0, 10000):
        sess.run(tranStep, feed_dict={x:dateNormal, y:priceNormal})  # 训练过程
    pred = sess.run(layer2, feed_dict={x:dateNormal})
    predPrice = np.zeros([15, 1])
    for i in range(0, 15):
        predPrice[i, 0] = (pred*3000)[i,0]
    plt.plot(date, predPrice, 'b', lw=1)

plt.show()