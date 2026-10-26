
import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    height, width = img.shape[:2]

    # Enlarge image 2 times
    bigger = cv2.resize(
        img, (width * 2, height * 2),
        interpolation=cv2.INTER_CUBIC
    )

    # Reduce image to half size
    smaller = cv2.resize(
        img, (width // 2, height // 2),
        interpolation=cv2.INTER_AREA
    )

    print("Original:", width, "x", height)
    print("Bigger:", bigger.shape[1], "x", bigger.shape[0])
    print("Smaller:", smaller.shape[1], "x", smaller.shape[0])

    # Show original image
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original Image", 400, 300)
    cv2.imshow("Original Image", img)

    # Show enlarged image
    cv2.namedWindow("Enlarged Image (2x)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Enlarged Image (2x)", 700, 500)
    cv2.imshow("Enlarged Image (2x)", bigger)

    # Show reduced image
    cv2.namedWindow("Reduced Image (0.5x)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Reduced Image (0.5x)", 250, 180)
    cv2.imshow("Reduced Image (0.5x)", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

