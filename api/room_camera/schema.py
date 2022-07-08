from pydantic import BaseModel, constr, StrictBool


class CameraRoom(BaseModel):
    camera_id: int
    room_id: int
