from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from settings.database import Base


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    emain: Mapped[str] = mapped_column(String, unique=True, nullable=False)
