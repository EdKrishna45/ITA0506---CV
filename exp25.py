import cv2
from tkinter import Tk, filedialog

Tk().withdraw()

file_path = filedialog.askopenfilename(
    title="Select Input Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

if not file_path:
    print("No input image selected!")
    exit()

ref_path = filedialog.askopenfilename(
    title="Select Reference Watch Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

if not ref_path:
    print("No reference image selected!")
    exit()

img = cv2.imread(file_path)
ref = cv2.imread(ref_path)

if img is None or ref is None:
    print("Unable to load image!")
    exit()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(gray_ref, None)
kp2, des2 = orb.detectAndCompute(gray_img, None)

if des1 is None or des2 is None:
    print("Watch not recognized!")
    cv2.imshow("Input Image", img)
else:
    matcher = cv2.BFMatcher(
        cv2.NORM_HAMMING,
        crossCheck=True
    )

    matches = matcher.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    if len(matches) >= 10:
        print("Watch Recognized!")
    else:
        print("Watch Not Recognized!")

    result = cv2.drawMatches(
        ref, kp1,
        img, kp2,
        matches[:30],
        None,
        flags=2
    )

    cv2.imshow("Watch Recognition", result)

cv2.waitKey(0)
cv2.destroyAllWindows()