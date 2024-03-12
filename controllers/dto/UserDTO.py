from pydantic import BaseModel, Field

from enum import Enum


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"


class UserDTO(BaseModel):
    firstname: str = Field(..., min_length=2, max_length=32)
    lastname: str = Field(..., min_length=2, max_length=32)
    age: int = Field(..., ge=14)
    weight: float = Field(..., le=200)
    height: float = Field(..., le=250)  # cm
    gender: Gender = Field(...)
    username: str = Field(..., min_length=5, max_length=16)
    password: str = Field(..., min_length=8, max_length=32)
