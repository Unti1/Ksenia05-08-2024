
from sqlalchemy import ARRAY, ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column
from models.enums import StatusEnum
from settings.database import Base, array_or_none_an


class Post(Base):
    title: Mapped[str]
    content: Mapped[Text]
    main_photo_url: Mapped[str]
    photo_urls: Mapped[array_or_none_an]
    status: Mapped[StatusEnum] = mapped_column(
        default=StatusEnum.PUBLISHED,
        server_default=text("'DRAFT'")
    )
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id')) # Подключение к внешнему ключу таблицы users по полю id
    