import cv2
import numpy

imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
img = cv2.imread(imageFn, 1)
imageInfo = img.shape
height, width, mode = imageInfo

# 灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 跟灰度图相同大小的目标图
dst = numpy.zeros((height, width, 1), numpy.uint8)


for h in range(0, height):
    for w in range(0, width - 1):
        gray1 = int(gray[h, w])
        gray2 = int(gray[h, w + 1])
        gray3 = gray1 - gray2 + 150
        if gray3 > 255:
            gray3 = 255
        if gray3 < 0:
            gray3 = 0
        dst[h, w] = gray3

cv2.imshow('dst', dst)
cv2.waitKey(0)

