import cv2



cap=cv2.VideoCapture(0)
if cap.isOpened():
    pass
index,image=cap.read()
cv2.imwrite('test.jpg',image)