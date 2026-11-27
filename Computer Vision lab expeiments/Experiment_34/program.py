import cv2, numpy as np
width=int(input("Enter image width: ")); height=int(input("Enter image height: "))
img=np.full((height,width,3),255,np.uint8)
cv2.circle(img,(width//2,height//2),min(width,height)//4,(255,0,0),3)
cv2.imwrite("output/circle.jpg",img)
print("Circle created")
