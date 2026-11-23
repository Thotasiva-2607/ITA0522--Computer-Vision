
import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (300, 200))

    result = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imshow("Original", img)
    cv2.imshow("270 Degree Clockwise", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
