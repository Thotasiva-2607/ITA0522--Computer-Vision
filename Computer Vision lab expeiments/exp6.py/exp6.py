
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found")
else:
    # Convert image to binary
    _, binary = cv2.threshold(
        img, 127, 255, cv2.THRESH_BINARY
    )

    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(binary, kernel, iterations=1)

    plt.subplot(1, 2, 1)
    plt.imshow(binary, cmap="gray")
    plt.title("Original Binary Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(eroded, cmap="gray")
    plt.title("Eroded Image")
    plt.axis("off")

    plt.show()
