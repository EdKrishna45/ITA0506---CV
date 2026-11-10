import cv2
import numpy as np

text = input("Enter the text: ")

image = np.ones((500, 800, 3), dtype=np.uint8) * 255

cv2.putText(
    image,
    text,
    (100, 250),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    (0, 0, 0),
    3
)

cv2.imshow("Text on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()