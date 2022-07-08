from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from api import db
from . import schema
from . import services
from . import validator
from api.users.schema import DisplayUser

router = APIRouter(tags=['TRVS'], prefix='/trvs')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_trv_registration(request: schema.Trv, database: Session = Depends(db.get_db)):

    trv = await validator.verify_ip_address(request.ip_address, database)

    if trv:
        raise HTTPException(
            status_code=400,
            detail="This ip address is already linked to a device"
        )

    new_trv = await services.new_trv_register(request, database)
    return new_trv


@router.get('/', response_model=List[schema.DisplayTrv])
async def get_all_trvs(database: Session = Depends(db.get_db)):
    return await services.all_trv(database)


@router.delete('/{trv_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_trv_by_id(trv_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_trv_by_id(trv_id, database)
