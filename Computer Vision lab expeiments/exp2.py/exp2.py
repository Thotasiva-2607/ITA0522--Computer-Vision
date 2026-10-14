
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
    plt.title("Gaussian Blur")
    plt.axis("off")

    plt.show()
