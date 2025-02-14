from services.create_admin import create_admin_if_not_exist
from config.logger_config import setupLogger

from db.database import get_session
from db.setup import create_db_and_tables
from fastapi import (
    FastAPI,
    APIRouter
)
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import auth_router

app = FastAPI()

router = APIRouter(prefix="/api/auth")

logger = setupLogger()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:80",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    create_db_and_tables()
    session=next(get_session())
    create_admin_if_not_exist(session)

router.include_router(auth_router)

app.include_router(router)
