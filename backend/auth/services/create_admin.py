from config.logger_config import setupLogger
from db.models.user import User
from fastapi_users.password import PasswordHelper
from sqlalchemy import select
from sqlalchemy.orm import Session

logger = setupLogger()

def create_admin_if_not_exist(session: Session):
    logger.info("Ensuring admin user exists...")

    stmt = select(User).where(User.email == "admin@example.com")
    user = session.execute(stmt).scalar_one_or_none()

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