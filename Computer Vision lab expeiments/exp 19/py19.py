
import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (300, 200))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.erode(gray, kernel, iterations=1)

    cv2.imshow("Original", gray)
    cv2.imshow("Erosion", erosion)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
