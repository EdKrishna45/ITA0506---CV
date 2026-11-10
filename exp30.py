import cv2

image = cv2.imread("face.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load smile detection Haar Cascade
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

# Detect smiles
smiles = smile_cascade.detectMultiScale(
    gray,
    scaleFactor=1.7,
    minNeighbors=20
)

# Draw rectangle around each smile
for (x, y, w, h) in smiles:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 0, 255),
        2
    )

# Display number of smiles
print("Number of smiles detected:", len(smiles))

# Display output
cv2.imshow("Smile Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()