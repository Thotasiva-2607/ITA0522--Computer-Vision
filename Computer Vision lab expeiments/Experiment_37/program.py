import cv2, numpy as np
img=cv2.imread("input/input_image.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
fg=cv2.inRange(hsv,np.array([0,60,40]),np.array([180,255,255]))
background=cv2.bitwise_and(img,img,mask=cv2.bitwise_not(fg))
cv2.imwrite("output/foreground_mask.jpg",fg)
cv2.imwrite("output/foreground_subtracted.jpg",background)
print("Foreground colour range: saturation >= 60")
