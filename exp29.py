import cv2

image = cv2.imread("face.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load eye detection Haar Cascade
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

# Draw rectangle around each eye
for (x, y, w, h) in eyes:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Display number of eyes
print("Number of eyes detected:", len(eyes))

# Display output
cv2.imshow("Eye Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()