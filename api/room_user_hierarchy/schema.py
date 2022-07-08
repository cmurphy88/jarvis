from pydantic import BaseModel, constr, StrictBool


class RoomUserHierarchy(BaseModel):
    room_id: int
    user_id: int
    user_order: int
