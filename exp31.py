import cv2

image = cv2.imread("images.jpg", 0)

if image is None:
    print("Error: Image not found.")
    raise SystemExit

threshold_value = int(input("Enter threshold value (0-255): "))

ret, segmented = cv2.threshold(
    image,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()