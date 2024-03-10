from pydantic import BaseModel

# TODO: add user profile fields
class UserDTO(BaseModel):
    username: str
    password: str
