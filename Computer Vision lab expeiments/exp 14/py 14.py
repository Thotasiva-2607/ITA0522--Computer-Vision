import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (300, 200))
    h, w = img.shape[:2]

    p1 = np.float32([
        [0, 0],
        [w, 0],
        [0, h],
        [w, h]
    ])

    p2 = np.float32([
        [60, 40],
        [240, 20],
        [20, 170],
        [280, 190]
    ])

    matrix = cv2.getPerspectiveTransform(p1, p2)

    result = cv2.warpPerspective(img, matrix, (w, h))

    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformation", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
