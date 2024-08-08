from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class SumRequest(BaseModel):
    a: float
    b: float

@router.post("/sum")
def sum_numbers(request: SumRequest):
    return {"result": request.a + request.b}

@router.get("/health")
def health_check():
    return {"status": "ok"}