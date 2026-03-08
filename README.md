## Drone Detection

SkyGuardian is a high-performance drone detection and tracking system built with YOLOv8, OpenCV, and NumPy.
It enables real-time identification, tracking, and trajectory analysis of unmanned aerial vehicles (UAVs) in diverse environments.

The system is designed for airspace monitoring, security applications, and experimental UAV tracking projects.

System Architecture

SkyGuardian operates using a three-layer processing pipeline:

Inference Layer

Powered by Ultralytics YOLOv8

Model trained on 10,000+ drone images

Supports YOLOv8-small / YOLOv8-medium

Processing Layer

OpenCV processes video frames

Handles:

Frame extraction

Bounding box rendering

Overlay drawing

3️Analysis Layer

NumPy performs:

Trajectory computation

Distance estimation

Velocity vector calculations

Key Features
Real-Time Detection

Optimized for 30+ FPS on GPU-enabled systems.

Distance Estimation

Uses triangle similarity to estimate drone distance from the camera.

Trajectory Tracking

Stores centroid history and visualizes movement path.

No-Fly Zone Alerts

Trigger notifications when a drone enters a restricted polygon area.

Movement Analysis

Calculates speed and direction vectors between frames.

Requirements
# Core Vision
ultralytics>=8.0.0
opencv-python>=4.8.0
numpy>=1.24.0

# Scientific Computing
matplotlib>=3.7.0

# Utilities
tqdm
python-dotenv
⚙ Installation
Clone the repository
git clone https://github.com/yourusername/skyguardian.git
cd skyguardian
Install dependencies
pip install -r requirements.txt
▶ Run Detection
python detect.py --source video.mp4 --weights best.pt

Supported sources:

video.mp4
webcam (0)
RTSP stream
IP camera​

If the displacement exceeds a defined threshold during time 
𝑡
t, the system triggers an Active Movement Event.

⚙ Configuration (config.yaml)

You can adjust system sensitivity without modifying code.

confidence_threshold: 0.45
iou_threshold: 0.5
classes: [4]
