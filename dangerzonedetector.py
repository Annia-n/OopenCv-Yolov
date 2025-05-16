import cv2
import pandas as pd
from ultralytics import YOLO
from datetime import datetime


model = YOLO('yolov8n.pt')


danger_zone = (200, 100, 500, 400)


alerts = []


cap = cv2.VideoCapture("/Users/anya/Downloads/document_5850222640903494861.mp4")
frame_id = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_id += 1
    results = model(frame, verbose=False)[0]


    cv2.rectangle(frame, (danger_zone[0], danger_zone[1]), (danger_zone[2], danger_zone[3]), (0, 0, 255), 2)
    cv2.putText(frame, 'Danger Zone', (danger_zone[0], danger_zone[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    for box in results.boxes:
        cls = int(box.cls[0])
        if cls == 0:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)


            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 3, (255, 0, 0), -1)


            if danger_zone[0] < cx < danger_zone[2] and danger_zone[1] < cy < danger_zone[3]:
                cv2.putText(frame, '!!! DANGER !!!', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                alerts.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "frame": frame_id,
                    "person_center": (cx, cy)
                })

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


df = pd.DataFrame(alerts)
df.to_csv("alerts.csv", index=False)
print(" هشدارها ذخیره شدند در فایل alerts.csv")

import os
print( os.path.abspath(__file__))