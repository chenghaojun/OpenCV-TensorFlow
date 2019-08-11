import cv2
import numpy as np

imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
img = cv2.imread(imageFn, 1)
imgInfo = img.shape  # (height, width)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]


dstImage = img[400:600, 800:1800]
cv2.imshow('dst', dstImage)
cv2.waitKey(0)