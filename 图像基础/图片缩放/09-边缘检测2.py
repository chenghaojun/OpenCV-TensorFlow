import cv2
import numpy as np
import random
import math

imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
img = cv2.imread(imageFn, 1)
cv2.imshow('img', img)

imgInfo = img.shape
height, width, mode = imgInfo

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 1), np.uint8)

# sobel 算法
# 1. sobel 卷积因子
# Gx         Gy
# -1 0 +1    +1 +2 +1
# -2 0 +2     0  0  0
# -1 0 +1    -1 -2 -1
# 2. 图片卷积 -> 计算梯度：根号（a²+b²）
# 3. 边缘判决
for h in range(0, height - 2):
    for w in range(0, width - 2):
        # y 方向上梯度的计算
        gy = gray[h, w] * 1 + gray[h, w+1] * 2 + gray[h, w+2] * 1 \
            - gray[h+2, w] * 1 - gray[h+2, w+1] * 2 - gray[h+2, w+2] * 1
        gx = gray[h, w] * 1 + gray[h+1, w] * 2 + gray[h+2, w] * 1 \
            - gray[h, w+2] * 1 - gray[h+1, w+2] * 2 - gray[h+2, w+2] * 1 

        # 梯度
        grad = math.sqrt(gy*gy + gx*gx)
        if grad > 50:
            dst[h, w] = 255
        else:
            dst[h, w] = 0

cv2.imshow('dst', dst)
cv2.waitKey(0)

