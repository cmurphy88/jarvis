from pydantic import BaseModel, constr, StrictBool


class RoomAlert(BaseModel):
    room_id: int
    message: str
