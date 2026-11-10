import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255

bh, bw = height // 10, width // 10

# Top-left black box
image[0:bh, 0:bw] = (0, 0, 0)

# Top-right blue box
image[0:bh, width-bw:width] = (255, 0, 0)

# Bottom-left green box
image[height-bh:height, 0:bw] = (0, 255, 0)

# Bottom-right red box
image[height-bh:height, width-bw:width] = (0, 0, 255)

cv2.imshow("Four Coloured Boxes", image)

cv2.waitKey(0)
cv2.destroyAllWindows()