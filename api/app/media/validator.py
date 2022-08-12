from typing import Optional

from sqlalchemy.orm import Session

from . models import Media
from pydantic import validate_email


async def verify_ip_address(ip_address: str, db_session: Session) -> Optional[Media]:
    return db_session.query(Media).filter(Media.ip_address == ip_address).first()
