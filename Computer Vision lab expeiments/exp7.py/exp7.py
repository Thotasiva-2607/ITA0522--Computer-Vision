import cv2

# Open the input video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video.mp4")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

# Create a normal-sized video window
window_name = "Computer Vision - Video Processing"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 450)

# Initial playback speed
speed = 1

print("Press 1 - Normal Motion")
print("Press 2 - Slow Motion")
print("Press 3 - Fast Motion")
print("Press Q - Exit")

while True:
    ret, frame = cap.read()

    if not ret:
        # Restart video when it reaches the end
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Resize frame to fit the window
    height, width = frame.shape[:2]
    scale = min(800 / width, 450 / height)

    new_width = int(width * scale)
    new_height = int(height * scale)

    frame = cv2.resize(frame, (new_width, new_height))

    # Display video
    cv2.imshow(window_name, frame)

    # Adjust playback delay
    if speed == 1:
        delay = int(1000 / fps)
    elif speed == 2:
        delay = int(3000 / fps)
    else:
        delay = max(1, int(1000 / (fps * 3)))

    # Read keyboard input
    key = cv2.waitKey(delay) & 0xFF

    if key == ord('1'):
        speed = 1
        print("Normal Motion")

    elif key == ord('2'):
        speed = 2
        print("Slow Motion")

    elif key == ord('3'):
        speed = 3
        print("Fast Motion")

    elif key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()

