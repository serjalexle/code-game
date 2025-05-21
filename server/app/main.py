from fastapi import FastAPI
from app.config.env import ENVSettings
from app.jobs.scheduler import start_scheduler
from app.utils.logger import logger

from fastapi.middleware.cors import CORSMiddleware
from app.config.database import init_db
from app.routes.index import APP_ROUTES

from app.sockets.battle_socket import sio
import socketio


async def lifespan(app: FastAPI):
    start_scheduler()

    for route in APP_ROUTES:
        app.include_router(route)
    try:
        await init_db()

        logger.success("APP STARTED SUCCESSFULLY")
        yield
    finally:
        logger.error("APP STOPPED")


# app = FastAPI(
#     title=ENVSettings.DOCS_TITLE,
#     description=ENVSettings.DOCS_DESCRIPTION,
#     version="0.1.0",
#     docs_url=ENVSettings.DOCS_URL if ENVSettings.DOCS_URL != "None" else None,
#     lifespan=lifespan,
# )

fastapi_app = FastAPI(
    title=ENVSettings.DOCS_TITLE,
    description=ENVSettings.DOCS_DESCRIPTION,
    version="0.1.0",
    docs_url=ENVSettings.DOCS_URL if ENVSettings.DOCS_URL != "None" else None,
    lifespan=lifespan,
)

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = socketio.ASGIApp(sio, fastapi_app)
