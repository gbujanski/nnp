from fastapi import APIRouter
from config.auth_config import (
    auth_backend,
    fastapi_users
)
from db.schemas.user import (
    UserCreate,
    UserRead,
    UserUpdate
)


auth_router = APIRouter()

auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=["auth"]
)

auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)

auth_router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["auth"],
)

auth_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    tags=["auth"],
)

auth_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)