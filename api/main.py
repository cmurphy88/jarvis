from fastapi import FastAPI
from api.users import router as user_router
from api.home import router as home_router
from api.room import router as room_router
from api.routine import router as routine_router
from api.camera import router as camera_router
# from api.home_user import router as home_user_router

app = FastAPI(title="JARVISWebApp",
              version="0.0.2")

app.include_router(user_router.router)
app.include_router(home_router.router)
app.include_router(room_router.router)
app.include_router(routine_router.router)
app.include_router(camera_router.router)
# app.include_router(home_router.router)

