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

kernel = np.ones((9, 9), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Black Hat Image", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()