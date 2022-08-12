from typing import Optional

from sqlalchemy.orm import Session

from . models import Camera


async def verify_camera_exist(ip_address: str, db_session: Session) -> Optional[Camera]:
    return db_session.query(Camera).filter(Camera.ip_address == ip_address).first()
