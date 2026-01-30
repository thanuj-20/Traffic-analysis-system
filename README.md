Indian Traffic Violation Detection System (YOLOv8 + ByteTrack)

A real-time computer vision system to detect, classify, and track Indian traffic vehicles and automatically identify red-light violations using YOLOv8 and multi-object tracking.

This project is designed for Indian road scenarios, handling mixed traffic such as cars, bikes, buses, trucks, and auto-rickshaws, with queue analysis near stop lines.

📌 Features

🚗 Multi-vehicle detection using YOLOv8 (Car, Bike, Bus, Truck)

🛺 Indian auto-rickshaw classification using custom aspect-ratio heuristics

🧠 Robust multi-object tracking with ByteTrack

🚨 Accurate red-light violation detection

Vehicle must cross the stop line forward

Eliminates false positives from overtaking or jitter

🚥 Queue detection near stop line

🎥 Slow-motion output video for better analysis

📊 Live metrics overlay

Queue count

Total violations


🛠️ Tech Stack
Component	Tool
Object Detection	YOLOv8 (Ultralytics)
Object Tracking	ByteTrack (Supervision)
Video Processing	OpenCV
Language	Python
Output	MP4 video with overlays


🧪 Detection Parameters
Parameter	Purpose
CONF_GENERAL = 0.30	General detection confidence
STOP_LINE_Y = 70% height	Red light stop line
QUEUE_Y_MIN = 55% height	Queue detection zone
imgsz = 1280	Better small object detection
YOLOv8m	Balanced accuracy + speed
🚨 Red Light Violation Logic
if prev_y < STOP_LINE_Y and cy > STOP_LINE_Y:
    violations.add(track_id)


✔️ Prevents:

False positives from overtaking

Stationary vehicles

Partial line touches

🛺 Indian Vehicle Classification

Auto-rickshaws are identified using:

Bounding box aspect ratio

Width constraint

YOLO class fallback

This improves accuracy in dense Indian traffic where COCO labels fail.

📊 Output Visualization

🟩 Green box → Normal vehicle

🟥 Red box → Red-light violation

🔴 Stop line marked clearly

📈 Live counters on video

🎯 Use Cases

Smart traffic monitoring

AI-based traffic law enforcement

Smart city surveillance

Hackathons & research demos

Computer vision portfolios

🚀 Future Enhancements

Traffic signal state detection

Helmet & seatbelt violation detection

License plate recognition

Speed estimation

Cloud deployment (Edge + CCTV)

Dashboard analytics
