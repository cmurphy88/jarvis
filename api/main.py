from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.users import router as user_router
from api.home import router as home_router
from api.room import router as room_router
from api.routine import router as routine_router
from api.camera import router as camera_router
from api.media import router as media_router
from api.trv import router as trv_router
from api.light import router as light_router
from api.auth import router as auth_router
from api.health import router as health_router
# from api.home_user import router as home_user_router

app = FastAPI(title="JARVISWebApp",
              version="0.0.2")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(home_router.router)
app.include_router(room_router.router)
app.include_router(routine_router.router)
app.include_router(camera_router.router)
app.include_router(media_router.router)
app.include_router(trv_router.router)
app.include_router(light_router.router)
app.include_router(health_router.router)

