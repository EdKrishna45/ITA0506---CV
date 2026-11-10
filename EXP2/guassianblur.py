
import cv2

# Read the input image
img = cv2.imread("flower.jpg")

if img is None:
    print("Error: Image not found")
else:
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(img, (15, 15), 0)

    # Save the blurred image
    cv2.imwrite("blur_flower.jpg", blurred)

    # Display the blurred image
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur Image", blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Gaussian Blur applied successfully")
