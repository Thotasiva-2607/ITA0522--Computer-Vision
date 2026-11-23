
import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (300, 200))

    overlay = img.copy()

    cv2.putText(
        overlay,
        "WATERMARK",
        (10, 180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    result = cv2.addWeighted(overlay, 0.4, img, 0.6, 0)

    cv2.imshow("Original", img)
    cv2.imshow("Watermarked Image", result)

    cv2.imwrite("watermarked_image.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
