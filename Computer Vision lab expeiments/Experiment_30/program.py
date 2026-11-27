import cv2
img=cv2.imread("input/face_sample.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_c=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
smile_c=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")
faces=face_c.detectMultiScale(gray,1.1,5)
out=img.copy(); total=0
for (x,y,w,h) in faces:
    roi=gray[y+int(h*.45):y+h,x:x+w]
    smiles=smile_c.detectMultiScale(roi,1.7,20,minSize=(20,10))
    total+=len(smiles)
    for (sx,sy,sw,sh) in smiles: cv2.rectangle(out,(x+sx,y+int(h*.45)+sy),(x+sx+sw,y+int(h*.45)+sy+sh),(0,255,0),2)
cv2.putText(out,f"Smiles detected: {total}",(15,35),cv2.FONT_HERSHEY_SIMPLEX,.8,(0,0,255),2)
cv2.imwrite("output/smile_detection.jpg",out)
print("Smiles detected:",total)
