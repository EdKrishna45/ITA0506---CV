import cv2

video = cv2.VideoCapture("reverse_video.mp4")

if not video.isOpened():
    print("Error: Video not found.")
    raise SystemExit

frames = []

while True:
    ret, frame = video.read()

    if not ret:
        break

    frames.append(frame)

video.release()

print("Total frames:", len(frames))
print("Playing video in reverse slow motion. Press Q to stop.")

for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion", frame)

    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

print("Video completed.")