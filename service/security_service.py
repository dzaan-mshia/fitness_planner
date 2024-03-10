import bcrypt
from fastapi import HTTPException

from service.jwt_utils import encode_jwt
from sqlalchemy.orm import Session

from controllers.dto.UserDTO import UserDTO
from db.models.User import User


class SecurityService:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def login(self, username: str, password: str):
        user = self.db_session.query(User).filter(User.username == username).first()  # TODO: check if user exists
        is_valid = self.verify_password(password, user.password)
        if is_valid:
            return encode_jwt({"user_id": user.id, "username": user.username})
        else:
            raise HTTPException(status_code=409, detail="Invalid username or password")

    def verify_password(self, plaintext_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plaintext_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def hash_password(self, password: str) -> str:
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def register_user(self, data: UserDTO):
        db_user = User(username=data.username, password=self.hash_password(data.password))
        self.db_session.add(db_user)
        self.db_session.commit()
        # TODO: add user profile entity and set it to user
