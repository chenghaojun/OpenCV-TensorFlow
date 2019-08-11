import cv2
import numpy as np

imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
img = cv2.imread(imageFn, 1)
imgInfo = img.shape  # (height, width)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

orgImgMat = np.asarray(img)

dstHegith = int(height)
dstWidth = int(width)

# 创建空白模板
dstImage = np.zeros((dstHegith, dstWidth, 3), np.uint8)  # 表示取值范围是 0-255
print(dstImage)

for i in range(0, dstHegith): # 行
    for j in range(0, dstWidth): # 列
        iNew = int(i * (height * 1.0/dstHegith))
        jNew = int(j * (width* 1.0/dstWidth))
        dstImage[i, j] = img[iNew, jNew]

cv2.imshow('dst', dstImage)
cv2.waitKey(0)