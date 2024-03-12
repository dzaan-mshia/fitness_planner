from pydantic import BaseModel, Field


class LoginDTO(BaseModel):
    username: str = Field(..., min_length=5, max_length=16)
    password: str = Field(..., min_length=8, max_length=32)
