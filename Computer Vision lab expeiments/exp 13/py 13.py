
import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (300, 200))
    h, w = img.shape[:2]

    p1 = np.float32([[0, 0], [w-1, 0], [0, h-1]])
    p2 = np.float32([[40, 30], [w-40, 50], [50, h-30]])

    matrix = cv2.getAffineTransform(p1, p2)

    result = cv2.warpAffine(img, matrix, (w, h))

    cv2.imshow("Original", img)
    cv2.imshow("Affine Transformation", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
