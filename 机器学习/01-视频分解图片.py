

# 视频分解图片
# 1. load, 2. info, 3. parse, 4. imshow, 5. imwrite

import cv2
import os

videoFn = 'c:/Users/admin/Desktop/dll/resources/juzuochizacai.mp4'
print(os.path.exists(videoFn))

cap = cv2.VideoCapture(videoFn)  # 获取视频打开句柄
isOpened = cap.isOpened()  # 当前文件是否可以打开
print(isOpened)

fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率，15帧以上才会显得流畅
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(fps, height, width)

i = 0

while (isOpened):
    if i == 10:
        break
    else:
        i = i + 1
    (flag, frame) = cap.read()  # 读取每一张图片
    if flag:
        fileName = 'C:/Users/admin/Desktop/dll/resources/image_%02d.jpg' % i
        print(fileName)
        cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
    else:
        print('error')

print('end')