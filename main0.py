import cv2
from jetcam.csi_camera import CSICamera

# 创建CSI摄像头对象
camera = CSICamera(width=640, height=480)

# 读取图像
image = camera.read()

# 保存图像
cv2.imwrite('photo.jpg', image)

# 释放摄像头资源
camera.release()
