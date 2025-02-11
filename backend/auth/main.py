
import logging
from typing import Optional
import uuid

from fastapi import FastAPI, Depends, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine, get_user_db
from db.models.user import Base, User
from db.schemas.user import UserCreate, UserRead, UserUpdate


from config.app_config import settings
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.password import PasswordHelper
from sqlalchemy.orm import Session
from sqlalchemy import select

app = FastAPI()
router = APIRouter(prefix="/api/auth")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if not logger.hasHandlers():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

logger.info("Logger is configured and ready to log messages.")

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

def create_db_and_tables():
    logger.info("Creating database and tables...")
    with engine.begin() as conn:
        Base.metadata.create_all(conn)
    logger.info("Database and tables created!")

def get_session():
    with Session(engine) as session:
        yield session

create_db_and_tables()

SECRET_KEY = settings.SECRET_KEY

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


cookie_transport = CookieTransport(
    cookie_max_age=60*60*24*365
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=60*60*24*365)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)

def ensure_admin_exists():
    logger.info("Ensuring admin user exists...")

    session = next(get_session())
    stmt = select(User).where(User.email == "admin@example.com")
    user = session.execute(stmt).first()
    if not user:
        fastapi_users_pw_helper = PasswordHelper()
        password = fastapi_users_pw_helper.generate()
        hashed_pass = fastapi_users_pw_helper.hash(password)
        user = User(
            email="admin@example.com",
            hashed_password=hashed_pass,
        )
        session.add(user)
        session.commit()
        logger.info(f"Admin user created! Email: admin@example.com, Password: {password}")
    else:
        logger.info("Admin user already exists. Skipping...")

@app.on_event("startup")
def startup_event():
    ensure_admin_exists()


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

current_active_user = fastapi_users.current_user(active=True, optional=True)

@router.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}"

@router.get("/")
def admin_protected_route(user: User = Depends(current_active_user)):
    return "hello admin"

app.include_router(router)