import cv2



cap=cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=30/1 ! nvvidconv  ! video/x-raw, width=1280, height=720, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink")
if cap.isOpened():
    pass
index,image=cap.read()
cv2.imwrite('test.jpg',image)