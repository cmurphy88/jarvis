from pydantic import BaseModel, constr, EmailStr, validate_email


class Room(BaseModel):
    name: constr(min_length=2, max_length=50)
    home_id: int


class DisplayRoom(BaseModel):
    id: int
    name: str
    home_id: int

    class Config:
        orm_mode = True
