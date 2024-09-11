from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def root():
    return {"message": "Hello to my FastAPI app!"}
