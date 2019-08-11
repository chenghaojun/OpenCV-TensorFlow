import tensorflow as tf

data1 = tf.constant([[6, 6]])
data2 = tf.constant([
    [2],
    [2]
])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([
    [1, 2],
    [3, 4],
    [5, 6]
])

matMul = tf.matmul(data1, data2)
matMul2 = tf.multiply(data2, data1)  # 跟自己维度相同的可以乘、符合矩阵乘法维度规则左列=右行的可以相乘。貌似符合交换律
matAdd = tf.add(data1, data3)

with tf.Session() as sess:
    # 这里有一个帮助记忆矩阵乘法维数的方法，维度：data1: M=1 N=2，data2: M=2, N=1

    print(sess.run(matMul))  
    print(sess.run(matMul2))
    print(sess.run(matAdd))
    print(sess.run([matMul, matAdd]))
