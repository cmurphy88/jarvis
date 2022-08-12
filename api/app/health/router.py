from fastapi import APIRouter, status
router = APIRouter(tags=['Health'], prefix='/health')


@router.post('/', status_code=status.HTTP_200_OK)
async def check_health():

    return
