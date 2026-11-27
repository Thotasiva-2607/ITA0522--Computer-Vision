import cv2
cap=cv2.VideoCapture("input/traffic_sample.mp4")
bg=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=25,detectShadows=False)
writer=None; count=0; last=None
while True:
    ok,frame=cap.read()
    if not ok: break
    mask=bg.apply(frame)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    out=frame.copy()
    for c in contours:
        x,y,w,h=cv2.boundingRect(c)
        if w*h>900:
            cv2.rectangle(out,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(out,"Vehicle",(x,max(20,y-8)),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,255,0),2)
    if writer is None: writer=cv2.VideoWriter("output/vehicle_detection.mp4",cv2.VideoWriter_fourcc(*"mp4v"),10,(frame.shape[1],frame.shape[0]))
    writer.write(out); last=out; count+=1
cap.release()
if writer: writer.release()
if last is not None: cv2.imwrite("output/vehicle_detection_frame.jpg",last)
print("Frames processed:",count)
