# OpenCV YOLOv8 Danger Zone Detector

**Overview**  
This project demonstrates how to use a YOLOv8 Nano model with OpenCV to detect predefined "danger zones" and log alerts when objects (or persons) enter those zones.

## Repository Structure
- `dangerzonedetector.py` – Main script for real-time detection and alerting.
- `yolov8n.pt` – Pretrained YOLOv8 Nano model (lightweight and optimized for speed).
- `alerts.csv` – Output CSV file capturing alert events (e.g., timestamp, detected object, zone).

## Requirements
- Python 3.x
- OpenCV (with DNN support):  
  ```bash
  pip install opencv-python
