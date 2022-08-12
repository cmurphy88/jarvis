from pydantic import BaseModel, constr, EmailStr, validate_email


class Camera(BaseModel):
    ip_address: str


class DisplayCamera(BaseModel):
    id: int
    ip_address: str

    class Config:
        orm_mode = True


class CameraRoom(BaseModel):
    camera_id: int
    room_id: int
