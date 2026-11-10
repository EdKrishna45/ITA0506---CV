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

watermark = img.copy()

cv2.putText(
    watermark,
    "OpenCV",
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", watermark)
cv2.waitKey(0)
cv2.destroyAllWindows()