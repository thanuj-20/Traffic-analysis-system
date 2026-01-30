!pip install -q ultralytics supervision opencv-python

import cv2
import numpy as np
from ultralytics import YOLO
import supervision as sv
from IPython.display import Video

model = YOLO("yolov8m.pt")  # better small-object detection

VIDEO_PATH = "/content/videoplayback.webm"
cap = cv2.VideoCapture(VIDEO_PATH)
assert cap.isOpened(), "Video not loaded"

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
OUTPUT_FPS = 10  # slow playback
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "/content/traffic_indian_fixed.mp4",
    fourcc,
    OUTPUT_FPS,
    (width, height)
)

tracker = sv.ByteTrack()
QUEUE_Y_MIN = int(height * 0.55)
STOP_LINE_Y = int(height * 0.70)
CONF_GENERAL = 0.30
CONF_STOPLINE = 0.20
violations = set()
last_positions = {}

def classify_indian_vehicle(x1, y1, x2, y2, cls_id):
    w = x2 - x1
    h = y2 - y1
    aspect = h / (w + 1e-5)
    # Auto-rickshaw heuristic
    if cls_id in [2, 5, 7] and aspect > 1.3 and w < 130:
        return "Auto"
    return {
        2: "Car",
        3: "Bike",
        5: "Bus",
        7: "Truck"
    }.get(cls_id, "Vehicle")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Dynamic confidence near stop line
    conf = CONF_GENERAL
    results = model(frame, conf=conf, imgsz=1280)[0]
    detections = sv.Detections.from_ultralytics(results)
    vehicle_classes = [2, 3, 5, 7]  # COCO vehicle IDs
    mask = np.isin(detections.class_id, vehicle_classes)
    detections = detections[mask]
    tracked = tracker.update_with_detections(detections)
    queue_count = 0
    for xyxy, track_id, cls_id in zip(
        tracked.xyxy,
        tracked.tracker_id,
        tracked.class_id
    ):
        x1, y1, x2, y2 = map(int, xyxy)
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        label = classify_indian_vehicle(x1, y1, x2, y2, cls_id)
        # Queue count
        if QUEUE_Y_MIN < cy < STOP_LINE_Y:
            queue_count += 1
        # ---- CORRECT RED LIGHT VIOLATION LOGIC ----
        if track_id in last_positions:
            prev_y = last_positions[track_id]
            # Must CROSS stop line forward
            if prev_y < STOP_LINE_Y and cy > STOP_LINE_Y:
                violations.add(track_id)
        last_positions[track_id] = cy
        # -----------------------------------------
        color = (0, 255, 0)
        if track_id in violations:
            color = (0, 0, 255)
            cv2.putText(
                frame,
                "RED LIGHT VIOLATION",
                (x1, y1 - 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(
            frame,
            f"{label} | ID {track_id}",
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 0),
            2
        )
    # Draw queue + stop line
    cv2.rectangle(frame, (0, QUEUE_Y_MIN), (width, STOP_LINE_Y), (255,255,0), 2)
    cv2.line(frame, (0, STOP_LINE_Y), (width, STOP_LINE_Y), (0,0,255), 3)
    # Metrics
    cv2.putText(frame, f"Queue Count: {queue_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.putText(frame, f"Violations: {len(violations)}",
                (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    out.write(frame)
cap.release()
out.release()
