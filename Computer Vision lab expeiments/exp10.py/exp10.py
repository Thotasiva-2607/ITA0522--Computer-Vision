
import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found! Keep image.jpg in the same folder.")
else:
    # Resize while maintaining the original aspect ratio
    height, width = img.shape[:2]
    new_width = 500
    new_height = int(height * new_width / width)

    img = cv2.resize(img, (new_width, new_height))

    # Rotate image 90 degrees clockwise
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Display original and rotated images
    cv2.imshow("1. ORIGINAL IMAGE", img)
    cv2.imshow("2. ROTATED IMAGE - 90 DEGREE CLOCKWISE", rotated)

    print("Original image size:", img.shape[1], "x", img.shape[0])
    print("Rotated image size:", rotated.shape[1], "x", rotated.shape[0])

    cv2.waitKey(0)
    cv2.destroyAllWindows()
