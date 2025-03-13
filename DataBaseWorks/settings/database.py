from datetime import datetime
from tokenize import String
from typing import Annotated, List
from sqlalchemy import ARRAY, Integer, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column, sessionmaker
from settings.config import settings

DATABASE_URL = settings.DATABASE_SQLITE

engine = create_engine(url = DATABASE_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

uniq_str_an = Annotated[str, mapped_column(unique=True)]
array_or_none_an = Annotated[List[str] | None, mapped_column(ARRAY(String))]
