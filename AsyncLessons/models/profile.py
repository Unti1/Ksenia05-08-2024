
from sqlalchemy import ForeignKey, text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
    contacts: Mapped[dict] = mapped_column(JSON)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True) 
    
    user: Mapped['User'] = relationship(
        'User',
        back_populates='profile',
        uselist=False,
    )