from pydantic import BaseModel, constr, StrictBool


class TrvRoom(BaseModel):
    trv_id: int
    room_id: int
