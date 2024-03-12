from fastapi import APIRouter, Depends

from controllers.dto.LoginDTO import LoginDTO
from controllers.dto.UserDTO import UserDTO
from service.jwt_utils import check_auth_token
from service.security_service import login_user, register_user

router = APIRouter(tags=["Authorization"])


@router.post("/login")
def login(data: LoginDTO):
    return login_user(data.username, data.password)


@router.delete("/logout")
def logout(auth_user_id: int = Depends(check_auth_token)):
    # TODO: delete access token from front-end and save sid into logout_sessions table; Periodically clean table from stale entries
    return {"message": " logout"}


@router.post("/register", status_code=201)
def registration(data: UserDTO):
    register_user(data)
