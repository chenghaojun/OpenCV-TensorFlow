import cv2

# open cv2 读取的图片路径中不能包含中文
imageFn = 'C:/Users/admin/Desktop/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
# 'C:/Users/admin/Desktop/dll/图像基础/图片缩放/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg'
with open(imageFn, 'rb') as f:
    print(f.read(10));

img = cv2.imread(imageFn, 1)  # 图片宽高
imageInfo = img.shape

width = imageInfo[0]
height = imageInfo[1]
mode = imageInfo[2]

# 
desHeight = int(height * 0.2)
dstWidth = int(width * 0.2)

# 最近邻域插值，双线性插值 像素关系重采样 立方插值
dst = cv2.resize(img, (desHeight, dstWidth))
cv2.imshow('image', dst)
cv2.waitKey(0)
