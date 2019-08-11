import cv2
import numpy

imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
img = cv2.imread(imageFn, 1)
cv2.imshow('img', img)

imageInfo = img.shape
height, width, mode = imageInfo

# 跟灰度图相同大小的目标图
dst = numpy.zeros((height, width, 3), numpy.uint8)


for h in range(0, height):
    for w in range(0, width):
        (b, g, r) = img[h, w]
        b = b * 1.5
        g = g * 1.3
        b = 255 if b > 255 else b
        g = 255 if g > 255 else g
        dst[h, w] = (b, g, r)

cv2.imshow('dst', dst)
cv2.waitKey(0)

