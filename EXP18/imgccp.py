import cv2
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

roi = img[50:200, 50:200]
h, w = roi.shape[:2]

if img.shape[0] >= 200 + h and img.shape[1] >= 200 + w:
    img[200:200+h, 200:200+w] = roi

cv2.imshow("ROI Cropping, Copying and Pasting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()