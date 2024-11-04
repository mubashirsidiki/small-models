# app\services\yolo_face_service.py
import cv2
import numpy as np
from typing import Dict
from ultralytics import YOLO

# Load YOLOv8 face detection model
model = YOLO('app/services/yolov8n-face.pt')

def detect_faces(image_bytes: bytes) -> Dict:
    # Decode image from bytes
    np_array = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Run YOLO model on the image
    results = model.predict(source=image, save=False, conf=0.25)
    detections = results[0].boxes.xyxy  # Face bounding boxes

    # Prepare face details
    faces_details = []
    for i, box in enumerate(detections):
        x1, y1, x2, y2 = map(int, box)
        faces_details.append({
            "face_id": i + 1,
            "bounding_box": {
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2
            }
        })
    
    return {
        "total_faces_detected": len(detections),
        "faces": faces_details
    }
