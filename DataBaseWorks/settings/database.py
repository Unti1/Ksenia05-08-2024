from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from settings.config import settings

DATABASE_URL = settings.DATABASE_SQLITE

engine = create_engine(url = DATABASE_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    __abstract__ = True # Чтобы не создавалась отдельная таблица для этого класса