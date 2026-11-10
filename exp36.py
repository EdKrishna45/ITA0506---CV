import cv2
import numpy as np

image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found.")
    raise SystemExit

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("Background Mask", mask)
cv2.imshow("Background Subtracted", result)

cv2.waitKey(0)
cv2.destroyAllWindows()