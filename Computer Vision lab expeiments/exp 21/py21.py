import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read input image
img = cv2.imread('image.jpg')

if img is None:
    print("Error: Image not found. Upload image.jpg")
else:
    # Resize image
    img = cv2.resize(img, (300, 200))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Opening operation (Erosion followed by Dilation)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

    # Display results
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(opening, cmap='gray')
    plt.title("Opening Operation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
