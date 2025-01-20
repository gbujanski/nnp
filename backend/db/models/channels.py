from sqlmodel import Field, SQLModel

class Channel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    