
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(filename):
    img = cv2.imread(filename)

    if img is None:
        print("Image not found")
        return

    # Split image into color channels
    colors = ("b", "g", "r")
    names = ("Blue", "Green", "Red")

    for i, color in enumerate(colors):
        hist = cv2.calcHist(
            [img], [i], None, [256], [0, 256]
        )

        plt.plot(hist, color=color, label=names[i])

    plt.title("Color Histogram")
    plt.xlabel("Intensity Level (0-255)")
    plt.ylabel("Pixel Count")
    plt.legend()
    plt.show()

analyze_histogram("image.jpg")
