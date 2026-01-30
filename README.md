Indian Traffic Violation Detection System (YOLOv8 + ByteTrack)

A real-time computer vision system to detect, classify, and track Indian traffic vehicles and automatically identify red-light violations using YOLOv8 and multi-object tracking.
This project is designed for Indian road scenarios, handling mixed traffic such as cars, bikes, buses, trucks, and auto-rickshaws, with queue analysis near stop lines.


📌 Features:
🚗 Multi-vehicle detection using YOLOv8 (Car, Bike, Bus, Truck)
🛺 Indian auto-rickshaw classification using custom aspect-ratio heuristics
🧠 Robust multi-object tracking with ByteTrack
🚨 Accurate red-light violation detection
 Vehicle must cross the stop line forward
 Eliminates false positives from overtaking or jitter
 🚥 Queue detection near stop line
 🎥 Slow-motion output video for better analysis
 📊 Live metrics overlay


🛠️ Tech Stack

Component	                        Tool
Object Detection	            YOLOv8 (Ultralytics)
Object Tracking	                ByteTrack (Supervision)
Video Processing	            OpenCV
Programming Language	        Python
Output	                        MP4 video with visual overlays


🛺 Indian Vehicle Classification

Auto-rickshaws are identified using:
Bounding box aspect ratio
Width constraint heuristics
YOLO class fallback mechanism
This significantly improves accuracy in dense Indian traffic, where standard COCO labels often fail.

📊 Output Visualization

🟩 Green bounding box → Normal vehicle
🟥 Red bounding box → Red-light violation
🔴 Stop line clearly marked
📈 Live counters displayed on video (queue count & violations)

🎯 Use Cases

Smart traffic monitoring systems
AI-based traffic law enforcement
Smart city surveillance solutions
Hackathons and research demonstrations
Computer vision portfolios

🚀 Future Enhancements

Traffic signal state detection
Helmet and seatbelt violation detection
License plate recognition
Speed estimation
Cloud / edge deployment (CCTV integration)
Analytics dashboard

📄 Project Documentation (Google Doc):
https://docs.google.com/document/d/1TO_wu279hTBEoxIMDgHH4nOj9X20sJsO/edit

🎥 Presentation / Demo Video (Loom):
https://www.loom.com/share/9aeb5c24a4a64c12883f6e46bfbe0b8b
