
import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (300, 200))

    # Select region of interest
    roi = img[50:150, 50:150]

    # Copy the selected region
    copied = roi.copy()

    # Paste into another location
    img[0:100, 0:100] = copied

    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Copied Region", copied)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
