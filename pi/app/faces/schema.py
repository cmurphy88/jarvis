from pydantic import BaseModel, constr, EmailStr, validate_email


class FindUser(BaseModel):
    user_id: int
