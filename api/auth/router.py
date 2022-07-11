from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api import db
from api.users import hashing
from api.users.models import User
from . import schema
from .auth_jwt import create_access_token

router = APIRouter(tags=["auth"])


@router.post('/login', response_model=schema.Token)
def login(request: schema.Login = Depends(), database: Session = Depends(db.get_db)):
    user = database.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    # Generate a JWT Token
    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
