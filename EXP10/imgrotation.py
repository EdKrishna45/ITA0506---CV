
import cv2
from tkinter import Tk, filedialog

# Hide Tkinter window
Tk().withdraw()

# Select an image
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

# Check if an image was selected
if not file_path:
    print("No image selected!")
    exit()

# Read the image
img = cv2.imread(file_path)

# Check if image loaded successfully
if img is None:
    print("Error: Unable to load image!")
    exit()

# Rotate the image 90 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("90 Degree Clockwise Rotated Image", rotated)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
