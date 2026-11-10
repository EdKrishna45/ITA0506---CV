import cv2
from tkinter import Tk, filedialog

# Hide Tkinter window
Tk().withdraw()

# Select video
file_path = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
)

if not file_path:
    print("No video selected!")
    exit()

# Open video
cap = cv2.VideoCapture(file_path)

if not cap.isOpened():
    print("Unable to open video!")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv2.CAP_PROP_FPS)

if fps == 0:
    fps = 25

# Read frames
frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Reverse frames
frames.reverse()

# Create output video
out = cv2.VideoWriter(
    "reverse_video.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

# Write reversed frames
for frame in frames:
    out.write(frame)

out.release()

print("Reverse video created successfully: reverse_video.mp4")

# Display reversed video
for frame in frames:
    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(int(1000 / fps)) & 0xFF == 27:
        break

cv2.destroyAllWindows()