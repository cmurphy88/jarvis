from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from api import db
from api.users import hashing, services
from api.users.models import User
from api.users import schema as user_schema
from api.users.validator import verify_email_exist
from .schema import Login

from .jwt import create_access_token

router = APIRouter(
    tags=['auth']
)


@router.post('/login')
def login(request: Login, database: Session = Depends(db.get_db)):
    user = database.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    # Generate a JWT Token
    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: user_schema.User, database: Session = Depends(db.get_db)):
    user = await verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system"
        )

    new_user = await services.new_user_register(request, database)
    return new_user
