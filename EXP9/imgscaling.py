
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

# Resize to a bigger size
bigger = cv2.resize(
    img, None, fx=2, fy=2,
    interpolation=cv2.INTER_LINEAR
)

# Resize to a smaller size
smaller = cv2.resize(
    img, None, fx=0.5, fy=0.5,
    interpolation=cv2.INTER_AREA
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
