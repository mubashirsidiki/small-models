# app/main.py

import uvicorn
from fastapi import FastAPI
from app.routers import flant5_router, yolo_face_router

app = FastAPI()

# Include routers
app.include_router(flant5_router.router, prefix="/flant5", tags=["FLAN-T5"])
app.include_router(yolo_face_router.router, prefix="/yolo-face", tags=["YOLO Face Detection"])

# Start Uvicorn server automatically when main.py is run
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
