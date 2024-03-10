import bcrypt
from fastapi import APIRouter

from controllers.dto.UserDTO import UserDTO
from db.conf.db_configuration import get_session
from db.models.User import User

router = APIRouter(tags=["Authorization"])


@router.post("/login")
def login():
    return {"message": "login success"}


@router.delete("/logout")
def get_user(user_id: int):
    return {"message": " logout"}


@router.post("/register")
def registration(data: UserDTO):
    db_session = next(get_session())
    db_user = User(username=data.username, password=hash_password(data.password))
    db_session.add(db_user)
    db_session.commit()
    # TODO: add user profile entity and set it to user



# TODO: move to service
def verify_password(plaintext_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plaintext_password.encode('utf-8'), hashed_password.encode('utf-8'))


def hash_password(password: str) -> str:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
