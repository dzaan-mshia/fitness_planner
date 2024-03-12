from pydantic import BaseModel

from enum import Enum


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"


class UserDTO(BaseModel):
    firstname: str
    lastname: str
    age: int
    weight: float
    height: float
    gender: Gender = None
    username: str
    password: str
