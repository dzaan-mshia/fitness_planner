from fastapi import APIRouter

router = APIRouter(tags=["Authorization"])


@router.post("/login")
def login():
    return {"message": "login success"}


@router.delete("/logout")
def get_user(user_id: int):
    return {"message": " logout"}


@router.post("/logout")
def registration(user_id: int):
    return {"message": " logout"}
