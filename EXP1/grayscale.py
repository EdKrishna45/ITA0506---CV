
import cv2

# Read the color image
img = cv2.imread("flower.jpg")

# Check whether the image was loaded
if img is None:
    print("Error: Image not found")
else:
    # Convert color image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("gray_flower.jpg", gray)

    # Display the grayscale image
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Grayscale image created successfully")
