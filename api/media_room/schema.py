from pydantic import BaseModel, constr, StrictBool


class MediaRoom(BaseModel):
    media_id: int
    room_id: int
