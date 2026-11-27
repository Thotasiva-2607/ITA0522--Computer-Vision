import cv2
cap=cv2.VideoCapture("input/traffic_sample.mp4"); frames=[]
while True:
    ok,frame=cap.read()
    if not ok: break
    frames.append(frame)
cap.release()
if not frames: raise RuntimeError("Video could not be read")
h,w=frames[0].shape[:2]
# 5 FPS playback makes the reversed video slow motion.
writer=cv2.VideoWriter("output/reverse_slow_motion.mp4",cv2.VideoWriter_fourcc(*"mp4v"),5,(w,h))
for frame in reversed(frames): writer.write(frame)
writer.release()
cv2.imwrite("output/reverse_slow_frame.jpg",frames[-1])
print("Frames:",len(frames)," | Output playback FPS: 5")
