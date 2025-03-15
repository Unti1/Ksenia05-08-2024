from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from settings.database import Base, uniq_str_an


class User(Base):
    username: Mapped[uniq_str_an]
    email: Mapped[uniq_str_an]
    password: Mapped[str]
    profile_id: Mapped[int | None] = mapped_column(ForeignKey('profiles.id'))
    
    # Подключаем связь для profiles
    profile: Mapped['Profile'] = relationship(
        'Profile',
        back_populates='user',
        uselist=False, #Ключевой параметр для связи один-к-одному, если не указать то связь становится один ко многим
        lazy='joined' # Автоматически будет подгружаться profile при запросе user
        
    )
    
    posts = Mapped['Post'] = relationship(
        'Post',
        back_populates='user',
        cascade='all, delete-orphan',  # Удаление всех связанных постов при удалении пользователя
    )
    
    