from sqlalchemy.dialects.postgresql import ARRAY
from settings.config import settings
from datetime import datetime
from typing import Annotated, List
from sqlalchemy import Integer, String, create_engine, func, select

from sqlalchemy.orm import DeclarativeBase, Mapped, Session, declared_attr, mapped_column, sessionmaker


DATABASE_URL = settings.get_db_url()

engine = create_engine(url = DATABASE_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)
        
        
def connection(method):
    def wrapper(*args, **kwargs):
        with session_maker() as session:
            try:
                return method(*args, session = session, **kwargs)
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
    return wrapper
        

class Base(DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'
    
    @classmethod
    @connection
    def get_by_id(cls, id: int, session: Session = None):
        rows = session.execute(select(cls).where(cls.id == id))
        obj = rows.scalars().first()
        return obj
        


uniq_str_an = Annotated[str, mapped_column(unique=True)]
array_or_none_an = Annotated[List[str], mapped_column(ARRAY(String))]
