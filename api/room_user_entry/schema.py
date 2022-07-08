from pydantic import BaseModel, constr, StrictBool


class RoomUserEntry(BaseModel):
    room_id: int
    user_id: int
