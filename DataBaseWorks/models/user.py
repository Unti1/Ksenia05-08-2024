from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship
from settings.database import Base, connection, uniq_str_an


class User(Base):
    username: Mapped[uniq_str_an]
    email: Mapped[uniq_str_an]
    password: Mapped[str]
    
    # Подключаем связь для profiles
    profile: Mapped['Profile'] = relationship(
        'Profile',
        back_populates='user',
        uselist=False, #Ключевой параметр для связи один-к-одному, если не указать то связь становится один ко многим
        lazy='joined' # Автоматически будет подгружаться profile при запросе user
    )
    
    posts : Mapped['Post'] = relationship(
        'Post',
        back_populates='user',
        cascade='all, delete-orphan',  
    )
    
    comment : Mapped['Comment'] = relationship(
        'Comment',
        back_populates='user',
        cascade='all, delete-orphan',  
    )

    
    @classmethod
    @connection
    def create_user(cls, username: str, email: str, password: str, session: Session = None):
        """Этот метод создает нового пользователя в базе данных.

        Args:
            username (str): имя пользователя
            email (str): электронная почта пользователя
            password (str): пароль пользователя
            session (Session, optional): db session. Defaults to None.

        Returns:
            User: новый созданный пользователь

        """
        new_user = User(username=username, email=email, password=password)
        session.add(new_user)
        session.commit()
        return new_user


        