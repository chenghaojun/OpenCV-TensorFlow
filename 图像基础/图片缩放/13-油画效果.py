import cv2
import numpy

imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
img = cv2.imread(imageFn, 1)
imageInfo = img.shape
height, width, mode = imageInfo

# 灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 目标区域
dst = numpy.zeros((height, width, 3), numpy.uint8)

for h in range(4, height - 4):
    for w in range(4, width - 4):
        array1 = numpy.zeros(8, numpy.uint8)
        for m in range(-4, 4):
            for n in range(-4, 4):
                p1 = int(gray[h + m, w + n]/32)
                array1[p1] = array1[p1] + 1
        currentMax = array1[0]
        l = 0
        for k in range(0, 8):
            if currentMax < array1[k]:
                currentMax = array1[k]
                l = k
        for m in range(-4, 4):
            for n in range(-4, 4):
                if gray[h + m, w + n] > (l*32) and gray[h + m, w+ n] <  ((l + 1)*32):
                    (b, g, r) = img[h + m, w + n]
        dst[h, w] = (b, g, r)

cv2.imshow('dst', dst)
cv2.waitKey(0)
