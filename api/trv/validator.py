from typing import Optional

from sqlalchemy.orm import Session

from . models import Trv
from pydantic import validate_email


async def verify_ip_address(ip_address: str, db_session: Session) -> Optional[Trv]:
    return db_session.query(Trv).filter(Trv.ip_address == ip_address).first()