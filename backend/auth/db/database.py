from sqlalchemy.engine import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import Session
from config.app_config import settings
from fastapi import Depends
from typing import AsyncGenerator
from fastapi_users.db import SQLAlchemyUserDatabase

from db.models.user import User

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
async_engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

def get_session():
    with Session(engine) as session:
        yield session

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)