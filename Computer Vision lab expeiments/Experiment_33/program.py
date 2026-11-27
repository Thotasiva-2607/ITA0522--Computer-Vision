import cv2, numpy as np
width=int(input("Enter image width: ")); height=int(input("Enter image height: "))
img=np.full((height,width,3),255,np.uint8)
cv2.rectangle(img,(width//4,height//4),(3*width//4,3*height//4),(0,0,255),3)
cv2.imwrite("output/rectangle.jpg",img)
print("Rectangle created")
