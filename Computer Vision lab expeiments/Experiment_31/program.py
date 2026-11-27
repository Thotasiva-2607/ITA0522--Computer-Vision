import cv2
img=cv2.imread("input/input_image.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,mask=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
seg=cv2.bitwise_and(img,img,mask=mask)
cv2.imwrite("output/threshold_mask.jpg",mask)
cv2.imwrite("output/segmented_image.jpg",seg)
print("Threshold value: 127")
print("Segmentation completed")
