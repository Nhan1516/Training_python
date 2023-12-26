from fastapi import APIRouter


router = APIRouter(
    tags=["USer Router"]
)


@router.get("/")
def get():
    return {'msg': 'Hello world'}