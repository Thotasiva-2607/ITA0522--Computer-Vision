
import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (300, 200))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    sx = cv2.convertScaleAbs(sx)
    sy = cv2.convertScaleAbs(sy)

    result = cv2.addWeighted(sx, 0.5, sy, 0.5, 0)

    cv2.imshow("Original", img)
    cv2.imshow("Sobel X", sx)
    cv2.imshow("Sobel Y", sy)
    cv2.imshow("Sobel Edge", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
