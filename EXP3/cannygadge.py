
import cv2
from tkinter import Tk, filedialog

# Select an image
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png")]
)
root.destroy()

if not file_path:
    print("No image selected")
else:
    # Read the image
    img = cv2.imread(file_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the result
    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edge Detection", edges)

    # Save the output
    cv2.imwrite("canny_edges.jpg", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Canny Edge Detection completed successfully")
