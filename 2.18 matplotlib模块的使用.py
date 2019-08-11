import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([3, 5, 7, 6, 2, 6, 10, 15])
print('1')
plt.plot(x, y, 'r', lw=1)  # 绘制折线图

print('2')

# 绘制柱状图

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([13, 15, 17, 16, 12, 16, 110, 115])
plt.bar(x, y, 0.2, alpha=1, color='b')
plt.show()