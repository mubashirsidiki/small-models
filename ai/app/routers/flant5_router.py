# app/routers/flant5_router.py
from fastapi import APIRouter, HTTPException
from app.services.flant5_service import generate_text
from app.schemas.flant5_schema import FLANT5Request, FLANT5Response

router = APIRouter()

@router.post("/generate-text", response_model=FLANT5Response)
async def generate_text_endpoint(request: FLANT5Request):
    try:
        generated_text = generate_text(request.prompt)
        return FLANT5Response(generated_text=generated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
