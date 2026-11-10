import cv2
import numpy as np
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

if not file_path:
    print("No image selected!")
    exit()

img = cv2.imread(file_path)

if img is None:
    print("Unable to load image!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(gray, kernel, iterations=1)

cv2.imshow("Original Image", gray)
cv2.imshow("Dilated Image", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()