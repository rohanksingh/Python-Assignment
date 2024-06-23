from fastapi import APIRouter, HTTPException
from app.models.addition import AdditionRequest, AdditionResponse
from app.controllers.addition_controller import create_addition_logic

router = APIRouter()

@router.post("/", response_model=AdditionResponse)
def create_addition(addition_request: AdditionRequest):
    try:
        return create_addition_logic(addition_request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
