import uuid
from datetime import timedelta, datetime

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

import jwt

SECRET_KEY = "swift-project"


def encode_jwt(payload: dict):
    payload.update({"exp": datetime.utcnow() + timedelta(hours=1)})
    payload.update({"sid": str(uuid.uuid4())})
    encoded_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return encoded_token


def decode_jwt(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])


def check_auth_token(token: str = Depends(HTTPBearer())) -> int:
    payload = decode_jwt(token.credentials)
    if payload["exp"] < datetime.utcnow().timestamp():
        raise HTTPException(401, detail="Session expired. Please Login again.")
    else:
        return payload["user_id"]
