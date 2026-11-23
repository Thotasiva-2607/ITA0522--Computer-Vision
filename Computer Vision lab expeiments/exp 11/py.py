import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Reduce image size to 400 x 300 pixels
    img = cv2.resize(img, (400, 300))

    result = cv2.rotate(img, cv2.ROTATE_180)

    cv2.imshow("Original Image", img)
    cv2.imshow("180 Degree Rotation", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
