

from sqlalchemy import ForeignKey, Text, text
from sqlalchemy.orm import Mapped, mapped_column
from models.enums import RatingEnum
from settings.database import Base


class Comment(Base):
    content: Mapped[Text]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    is_published: Mapped[bool] = mapped_column(default=True, server_default=text("'false'"))
    rating: Mapped[RatingEnum] = mapped_column(default=RatingEnum.FIVE, server_default=text("'SEVEN'"))

