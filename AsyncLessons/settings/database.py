from datetime import datetime
from typing import Annotated, Any, Dict, List, Self

from sqlalchemy import String, func, select
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    class_mapper,
    declared_attr,
    mapped_column,
)

from settings.config import settings

DATABASE_URL = settings.get_async_db_url()

engine = create_async_engine(url = DATABASE_URL)
session_maker = async_sessionmaker(engine, expire_on_commit=False)
        
        
def connection(method):
    async def wrapper(*args, **kwargs):
        async with session_maker() as session:
            try:
                return await method(*args, session = session, **kwargs)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()
    return wrapper
        

class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'
    
    
    @classmethod
    @connection
    async def add(cls,
            session: AsyncSession = None,
            **values) -> Self:
        new_instance = cls(**values)
        session.add(new_instance)
        try:
            await session.commit()
        except Exception as e:
            session.rollback()
            raise e
        return new_instance

    @classmethod
    @connection
    async def add_many(cls,
                 instances: List[Dict[str, Any]], 
                 session: AsyncSession = None) -> List[Self]:
        new_instances = [cls(**values) for values in instances]
        session.add_all(new_instances)
        try:
            await session.commit()
        except Exception as e:
            session.rollback()
            raise e
        return new_instances
    
    @classmethod
    @connection
    async def update_per_id(cls,
                    id: int,
                    session: AsyncSession = None,
                    **instance: Dict[str, Any]):
        
        rows = await session.execute(select(cls).where(cls.id == id))
        concrete_row = rows.scalars().first()
        
        if not concrete_row:
            return None
        
        changed = False
        for key, value in instance.items():
            if getattr(concrete_row, key) != value:
                setattr(concrete_row, key, value)
                changed = True
        
        if changed:
            await session.commit()
        
        return concrete_row
        
    @classmethod
    @connection
    async def delete_per_id(cls,
                    id: int,
                    session: AsyncSession = None):
        
        rows = await session.execute(select(cls).where(cls.id == id))
        concrete_row = rows.scalars().first()
        if not concrete_row:
            return False
        
        session.delete(concrete_row)
        await session.commit()
        return True    
    
    @classmethod
    @connection
    async def get_by_id(cls, id: int, session: AsyncSession = None):
        rows = await session.execute(select(cls).where(cls.id == id))
        obj = rows.scalars().first()
        return obj
    
    
    @classmethod
    @connection
    async def get_all(cls, session: AsyncSession = None):
        rows = await session.execute(select(cls))
        objs = rows.scalars().all()
        return objs


    
    def to_dict(self) -> dict:
        columns = class_mapper(self.__class__).columns
        return {column.key: getattr(self, column.key) for column in columns}

uniq_str_an = Annotated[str, mapped_column(unique=True)]
array_or_none_an = Annotated[List[str], mapped_column(ARRAY(String), default=[])]
