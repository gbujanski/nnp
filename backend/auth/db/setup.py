from config.logger_config import setupLogger
from db.database import engine
from db.models.user import Base

logger = setupLogger()

def create_db_and_tables():
    logger.info("Creating database and tables...")
    with engine.begin() as conn:
        Base.metadata.create_all(conn)
    logger.info("Database and tables created!")
    