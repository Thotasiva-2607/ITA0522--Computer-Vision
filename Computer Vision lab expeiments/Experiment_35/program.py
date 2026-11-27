import cv2, numpy as np
text=input("Enter text to display: ")
img=np.full((420,640,3),255,np.uint8)
cv2.putText(img,text,(25,210),cv2.FONT_HERSHEY_SIMPLEX,.9,(0,0,0),2,cv2.LINE_AA)
cv2.imwrite("output/text_on_image.jpg",img)
print("Text added:",text)
