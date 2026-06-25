import cv2
from ultralytics import YOLO
import json

# Load model
model = YOLO("yolov8n.pt")

# Load video
video_path = "monitor/videos/input.mp4"
cap = cv2.VideoCapture(video_path)

output = []
alerts = []

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    people_count = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])

            if label == "person":
                people_count += 1

            output.append({
                "frame": frame_count,
                "object": label,
                "confidence": conf
            })

            # Draw box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    # 🚨 Alert logic
    if people_count > 5:
        alerts.append({
            "frame": frame_count,
            "alert": "Overcrowding detected"
        })

    cv2.imshow("AI Video Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()

# Save results
with open("monitor/data/output.json", "w") as f:
    json.dump(output, f, indent=4)

with open("monitor/data/alerts.json", "w") as f:
    json.dump(alerts, f, indent=4)

print("✅ Video processed successfully")