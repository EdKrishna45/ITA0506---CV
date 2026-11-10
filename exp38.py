import cv2

image = cv2.imread("group.jpg")

if image is None:
    print("Error: Image not found.")
    raise SystemExit

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

print("Number of faces detected:", len(faces))

cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()