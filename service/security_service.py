import bcrypt
from fastapi import HTTPException

from db.service.UserDB import get_user_by_username, save_user
from service.jwt_utils import encode_jwt

from controllers.dto.UserDTO import UserDTO


def login_user(username: str, password: str):
    user_id, hashed_password = get_user_by_username(username)

    is_valid = verify_password(password, hashed_password)
    if is_valid:
        return encode_jwt({"user_id": user_id, "username": username})
    else:
        raise HTTPException(status_code=409, detail="Invalid username or password")


def verify_password(plaintext_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plaintext_password.encode('utf-8'), hashed_password.encode('utf-8'))


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def register_user(data: UserDTO):
    data.password = hash_password(data.password)
    save_user(data)
