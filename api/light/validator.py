from typing import Optional

from sqlalchemy.orm import Session

from . models import Light
from pydantic import validate_email


async def verify_ip_address(ip_address: str, db_session: Session) -> Optional[Light]:
    return db_session.query(Light).filter(Light.ip_address == ip_address).first()
