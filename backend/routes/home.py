from fastapi import APIRouter

#create a fastapi app
router = APIRouter()

# Define a route for the home page
@router.get("/")
def root():
    return {"message": "Hello to my FastAPI app!"}