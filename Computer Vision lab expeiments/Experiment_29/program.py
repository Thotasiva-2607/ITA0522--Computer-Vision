import cv2
img=cv2.imread("input/face_sample.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_c=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_c=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
faces=face_c.detectMultiScale(gray,1.1,5)
out=img.copy(); total=0
for (x,y,w,h) in faces:
    roi=gray[y:y+h,x:x+w]; eyes=eye_c.detectMultiScale(roi,1.1,5)
    total+=len(eyes)
    for (ex,ey,ew,eh) in eyes: cv2.rectangle(out,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)
cv2.putText(out,f"Eyes detected: {total}",(15,35),cv2.FONT_HERSHEY_SIMPLEX,.8,(0,0,255),2)
cv2.imwrite("output/eye_detection.jpg",out)
print("Eyes detected:",total)
