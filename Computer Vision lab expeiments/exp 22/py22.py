import cv2
import numpy as np

# Read image (keep image.jpg in the same folder as your Python file)
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found! Check the image path.")
else:
    img = cv2.resize(img, (300, 200))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("Original Image", gray)
    cv2.imshow("Morphological Closing", closing)

    print("Press any key on the image window to close.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
