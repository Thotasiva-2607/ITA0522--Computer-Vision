import cv2, numpy as np
img=cv2.imread("input/input_image.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# Background is defined here as low-saturation, high-value pixels.
bg=cv2.inRange(hsv,np.array([0,0,190]),np.array([180,70,255]))
foreground=cv2.bitwise_and(img,img,mask=cv2.bitwise_not(bg))
cv2.imwrite("output/background_mask.jpg",bg)
cv2.imwrite("output/background_subtracted.jpg",foreground)
print("Background colour range: low saturation, value 190-255")
