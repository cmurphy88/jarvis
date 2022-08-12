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


class RoomAlert(BaseModel):
    room_id: int
    message: str


class RoomUserHierarchy(BaseModel):
    room_id: int
    user_id: int
    user_order: int


class RoomUserEntry(BaseModel):
    room_id: int
    user_id: int

