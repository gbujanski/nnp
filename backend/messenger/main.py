from typing import Union
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from db.models.channels import Channel
from sqlmodel import Session, select, SQLModel
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine

app = FastAPI()
router = APIRouter(prefix="/api/messenger")


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
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

create_db_and_tables()

# this endpint is used to triggger auth verify in api gateway
@router.get("/status")
def get_status():
    return {"status": "ok"}


@router.post("/channel")
def create_channel(channel: Channel, session: Session = Depends(get_session)):
    session.add(channel)
    session.commit()
    session.refresh(channel)
    return channel

@router.get("/channels")
def get_all_channels(session: Session = Depends(get_session)) -> list[Channel]:
    stmt = select(Channel)
    result = session.exec(stmt)
    return result


@router.delete("/channel/{channel_id}")
def delete_channel(channel_id: int, session: Session = Depends(get_session)):
    channel = session.get(Channel, channel_id)
    if (not channel):
        raise HTTPException(status_code=404, detail="Channel not found")
    session.delete(channel)
    session.commit()
    return {"message": "Channel deleted successfully"}

app.include_router(router)
