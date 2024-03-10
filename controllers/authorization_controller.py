import bcrypt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.dto.LoginDTO import LoginDTO
from controllers.dto.UserDTO import UserDTO
from db.conf.db_configuration import get_session
from service.jwt_utils import check_auth_token
from service.security_service import SecurityService

router = APIRouter(tags=["Authorization"])
security_service = SecurityService(get_session())


@router.post("/login")
def login(data: LoginDTO):
    return security_service.login(data.username, data.password)


@router.delete("/logout")
def logout(auth_user_id: int = Depends(check_auth_token)):
    return {"message": " logout"}


@router.post("/register", status_code=201)
def registration(data: UserDTO):
    security_service.register_user(data)
