from sqlmodel import create_engine
from config.app_config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
