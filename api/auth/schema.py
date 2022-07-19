from typing import Optional

from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str
    grant_type: str = "password"


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
