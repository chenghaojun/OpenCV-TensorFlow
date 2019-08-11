import cv2
import numpy as np

imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
img = cv2.imread(imageFn, 1)
imageInfo = img.shape
height, width, mode = imageInfo

# 高斯滤波
# dst = cv2.GaussianBlur(img, (5, 5), 1.5)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)


# 均值滤波
dst = np.zeros((height, width, 3), np.uint8)

for h in range(3, height - 3):
    for w in range(3, width - 3):
        sumB = int(0)
        sumG = int(0)
        sumR = int(0)
        for m in range(-3, 3): # -3 -2 -1 0 1 2
            for n in range(-3, 3):
                b, g, r = img[h + m, w + n]
                sumB += b
                sumG += g
                sumR += r
        b = np.uint8(sumB/36)
        g = np.uint8(sumB/36)
        r = np.uint8(sumB/36)

        dst[h, w] = (b, g, r)

cv2.imshow('dst', dst)
cv2.waitKey(0)

# 中值滤波
