from typing import Union
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from db.models.channels import Channel
from sqlmodel import Session, select, SQLModel
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/channel")
def create_channel(channel: Channel, session: Session = Depends(get_session)):
    session.add(channel)
    session.commit()
    session.refresh(channel)
    return channel

@app.get("/channels")
def get_all_channels(session: Session = Depends(get_session)) -> list[Channel]:
    stmt = select(Channel)
    result = session.exec(stmt)
    return result


@app.delete("/channel/{channel_id}")
def delete_channel(channel_id: int, session: Session = Depends(get_session)):
    channel = session.get(Channel, channel_id)
    if (not channel):
        raise HTTPException(status_code=404, detail="Channel not found")
    session.delete(channel)
    session.commit()
    return {"message": "Channel deleted successfully"}