# app/schemas/flant5_schema.py
from pydantic import BaseModel

class FLANT5Request(BaseModel):
    prompt: str

class FLANT5Response(BaseModel):
    generated_text: str
