# app/schemas/yolo_face_schema.py
from typing import List
from pydantic import BaseModel

class FaceBoundingBox(BaseModel):
    x1: int
    y1: int
    x2: int
    y2: int

class FaceDetail(BaseModel):
    face_id: int
    bounding_box: FaceBoundingBox

class YOLOFaceResponse(BaseModel):
    total_faces_detected: int
    faces: List[FaceDetail]
