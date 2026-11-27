import cv2, pytesseract
cap=cv2.VideoCapture("input/text_video.mp4")
all_text=[]
while True:
    ok,frame=cap.read()
    if not ok: break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    text=pytesseract.image_to_string(gray,config="--psm 6").strip()
    if text and text not in all_text: all_text.append(text)
cap.release()
with open("output/extracted_text.txt","w",encoding="utf-8") as f: f.write("\\n".join(all_text))
print("Extracted text:")
print("\\n".join(all_text))
