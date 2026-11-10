from ultralytics import YOLO
import cv2

# Load YOLO model
print("Loading YOLO model...")
model = YOLO("yolov8n.pt")
print("Model loaded successfully.")

# Open video
video_path = r"vehicles.mp4"
cap = cv2.VideoCapture(video_path)

# Check video
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("Video opened successfully.")
print("Press Q to stop the video.")

# Create resizable window
cv2.namedWindow("Vehicle Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Vehicle Detection", 1000, 700)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video finished.")
        break

    # Detect objects
    results = model(frame, verbose=False)

    # Process detections
    for result in results:
        if result.boxes is None:
            continue

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            if class_id in [2, 3, 5, 7]:
                x1, y1, x2, y2 = map(
                    int, box.xyxy[0]
                )

                if class_id == 2:
                    vehicle_name = "Car"
                elif class_id == 3:
                    vehicle_name = "Motorcycle"
                elif class_id == 5:
                    vehicle_name = "Bus"
                else:
                    vehicle_name = "Truck"

                # Draw rectangle
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                # Display label
                label = vehicle_name + " " + str(
                    round(confidence * 100, 1)
                ) + "%"

                cv2.putText(
                    frame,
                    label,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    # Resize frame
    height, width = frame.shape[:2]

    max_width = 1000
    max_height = 700

    scale = min(
        max_width / width,
        max_height / height
    )

    new_width = int(width * scale)
    new_height = int(height * scale)

    resized_frame = cv2.resize(
        frame,
        (new_width, new_height)
    )

    cv2.imshow("Vehicle Detection", resized_frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Vehicle detection completed.")