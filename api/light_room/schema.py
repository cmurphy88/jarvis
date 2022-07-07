from pydantic import BaseModel, constr, StrictBool


class LightRoom(BaseModel):
    light_id: int
    room_id: int
