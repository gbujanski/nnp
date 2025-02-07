from sqlmodel import create_engine
from config.app_config import settings

from db.models.channels import Channel

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
