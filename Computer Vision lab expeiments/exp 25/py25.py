
import cv2

# Read the reference watch image
watch = cv2.imread("watch.jpg", 0)

# Read the main image
img = cv2.imread("image.jpg")

if watch is None or img is None:
    print("Images not found!")
else:
    img = cv2.resize(img, (300, 200))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize watch template
    watch = cv2.resize(watch, (50, 50))

    # Template matching
    result = cv2.matchTemplate(
        gray, watch, cv2.TM_CCOEFF_NORMED
    )

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Draw rectangle around detected object
    h, w = watch.shape

    x, y = max_loc

    cv2.rectangle(
        img, (x, y), (x+w, y+h),
        (0, 255, 0), 2
    )

    cv2.imshow("Watch Recognition", img)

    print("Match Score:", max_val)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
