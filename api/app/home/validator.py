from typing import Optional

from sqlalchemy.orm import Session

from . models import Home
from pydantic import validate_email


async def verify_home_exist(home: str, db_session: Session) -> Optional[Home]:
    return db_session.query(Home).filter(Home.name == home).first()
