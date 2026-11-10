import cv2
import pytesseract

# If Tesseract is not automatically detected, set its path:
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

video = cv2.VideoCapture("krishna.mp4")

if not video.isOpened():
    print("Error: Video not found.")
    raise SystemExit

print("Extracting text from video. Press Q to stop.")

while True:
    ret, frame = video.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    if text.strip():
        print("Extracted Text:")
        print(text)

    cv2.imshow("Text Extraction from Video", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

print("Text extraction completed.")