# app\routers\yolo_face_router.py
from app.services.yolo_face_service import detect_faces
from app.schemas.yolo_face_schema import YOLOFaceResponse
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

@router.post("/detect-faces", response_model=YOLOFaceResponse)
async def detect_faces_endpoint(file: UploadFile = File(...)):
    try:
        # Read file content as bytes
        image_bytes = await file.read()
        # Run face detection
        face_data = detect_faces(image_bytes)
        return YOLOFaceResponse(**face_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
