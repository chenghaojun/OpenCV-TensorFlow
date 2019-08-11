import cv2
import numpy as np
import random

imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
img = cv2.imread(imageFn, 1)
cv2.imshow('img', img)

imgInfo = img.shape
height, width, mode = imgInfo
print(height, width, mode)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图片
cv2.imshow('gray', gray)

imgG = cv2.GaussianBlur(gray, (3, 3), 0)  # 高斯滤波

dst = cv2.Canny(img, 50, 50)  # 边缘检测
cv2.imshow('dst', dst)

cv2.waitKey(0)


