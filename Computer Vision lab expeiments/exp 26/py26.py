import cv2

cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Video not found!")
else:
    frames = []

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 25

    # Read video frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (300, 200))
        frames.append(frame)

    cap.release()

    # Reverse frames
    frames.reverse()

    # Save reverse video
    out = cv2.VideoWriter(
        "reverse_video.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (300, 200)
    )

    for frame in frames:
        out.write(frame)

    out.release()

    print("Reverse video saved successfully!")

    # Play reverse video
    cap = cv2.VideoCapture("reverse_video.mp4")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Reverse Video", frame)

        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
