from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class SumRequest(BaseModel):
    o: str
    a: float
    b: float

def sum_ab(a,b):
    return a+b

@router.post("/sum")
def operations(request: SumRequest):
    result=0
    if request.o=='+':
        result=sum_ab(request.a,request.b)
    return {"result": result}

@router.get("/health")
def health_check():
    return {"status": "ok"}