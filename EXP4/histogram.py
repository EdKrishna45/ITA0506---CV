
import cv2

# Read the input image
img = cv2.imread("flower.jpg")

if img is None:
    print("Error: Image not found")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display the images
    cv2.imshow("Original Grayscale Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    # Save the output image
    cv2.imwrite("equalized_flower.jpg", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Histogram Equalization completed successfully")
