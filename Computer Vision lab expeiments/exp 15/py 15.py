
import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (300, 200))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    corners = cv2.dilate(corners, None)

    result = img.copy()
    result[corners > 0.01 * corners.max()] = [0, 0, 255]

    cv2.imshow("Original", img)
    cv2.imshow("Harris Corner Detection", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
