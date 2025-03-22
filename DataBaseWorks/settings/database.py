from sqlalchemy.dialects.postgresql import ARRAY
from settings.config import settings
from datetime import datetime
from typing import Annotated, Any, Dict, List, Self
from sqlalchemy import Integer, String, create_engine, func, select

from sqlalchemy.orm import DeclarativeBase, Mapped, Session, class_mapper, declared_attr, mapped_column, sessionmaker


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
    
    @classmethod
    @connection
    def add(cls,
            session:Session = None,
            **values) -> Self:
        new_instance = cls(**values)
        session.add(new_instance)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        return new_instance

    
    @classmethod
    @connection
    def add_many(cls,
                 instances: List[Dict[str, Any]], 
                 session: Session = None) -> List[Self]:
        new_instances = [cls(**values) for values in instances]
        session.add_all(new_instances)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        return new_instances
    
    @classmethod
    @connection
    def update_per_id(cls,
                    id: int,
                    session: Session = None,
                    **instance: Dict[str, Any]):
        
        rows = session.execute(select(cls).where(cls.id == id))
        concrete_row = rows.scalars().first()
        
        if not concrete_row:
            return None
        
        changed = False
        for key, value in instance.items():
            if getattr(concrete_row, key) != value:
                setattr(concrete_row, key, value)
                changed = True
        
        if changed:
            session.commit()
        
        return concrete_row
        

    @classmethod
    @connection
    def update_per_id(cls,
                    id: int,
                    session: Session = None):
        
        rows = session.execute(select(cls).where(cls.id == id))
        concrete_row = rows.scalars().first()
        if not concrete_row:
            return False
        
        session.delete(concrete_row)
        session.commit()
        return True    
    
    def to_dict(self) -> dict:
        columns = class_mapper(self.__class__).columns
        return {column.key: getattr(self, column.key) for column in columns}

uniq_str_an = Annotated[str, mapped_column(unique=True)]
array_or_none_an = Annotated[List[str], mapped_column(ARRAY(String), default=[])]
