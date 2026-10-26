import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found")
else:
    # Convert to binary image
    _, binary = cv2.threshold(
        img, 127, 255, cv2.THRESH_BINARY
    )

    # Create a smaller kernel
    kernel = np.ones((3, 3), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(
        binary, kernel, iterations=1
    )

    # Resize images for display
    original_small = cv2.resize(binary, (400, 300))
    dilated_small = cv2.resize(dilated, (400, 300))

    # Display images
    cv2.imshow("Original Image", original_small)
    cv2.imshow("Dilated Image", dilated_small)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
