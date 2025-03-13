from tokenize import String
from typing import List
from sqlalchemy import ARRAY, text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column
from models.enums import GenderEnum, ProfessionEnum
from settings.database import Base, array_or_none_an


class Profile(Base):
    name: Mapped[str]
    surname: Mapped[str|None]
    age: Mapped[int|None]
    gender: Mapped[GenderEnum]
    profession: Mapped[ProfessionEnum] = mapped_column(
        default=ProfessionEnum.UNEMPLOYED, # default - это те значениея которые выставляются нашим кодом
        server_default=text("'UNEMPLOYED'") # server default - это то значение которое будет устанавливаться в базе данных при создании нового объекта(если из кода значения не поступило)
    )
    interests: Mapped[array_or_none_an]
    contacts: Mapped[dict | None] = mapped_column(JSON)