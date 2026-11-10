
import cv2
import numpy as np
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

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(img, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
