import cv2
import numpy as np

face_xml = cv2.CascadeClassifier('c:/Users/admin/Desktop/dll/resources/haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier('c:/Users/admin/Desktop/dll/resources/haarcascade_eye.xml')

# load img

# imgFn = 'C:/Users/admin/Desktop/dll/resources/image_%02d.jpg' % 1
imgFn = 'C:/Users/admin/Desktop/dll/resources/zhengjianzhaoshibie11.jpg'
img = cv2.imread(imgFn)
cv2.imshow('img', img)

# haar gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect
faces = face_xml.detectMultiScale(gray, 1.3, 5)  # 灰度图
print('face = ', len(faces))

# draw
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_face = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_xml.detectMultiScale(roi_face)
    print('eyes = ', len(eyes))
    for (eX, eY, eW, eH) in eyes:
        cv2.rectangle(roi_color, (eX, eY), (eX + eW, eY + eH), (0, 255, 0), 2)

cv2.imshow('dst', img)
cv2.waitKey(0)
