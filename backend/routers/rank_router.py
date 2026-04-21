from fastapi import APIRouter

router = APIRouter()

@router.get("/rank")
def get_rank():
    return {"message": "ranking data"}