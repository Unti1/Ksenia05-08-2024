
from sqlalchemy import ARRAY, ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship
from models.enums import StatusEnum
from settings.database import Base, array_or_none_an, connection


class Post(Base):
    title: Mapped[str]
    content: Mapped[str] = mapped_column(Text)
    main_photo_url: Mapped[str]
    photo_urls: Mapped[array_or_none_an]
    status: Mapped[StatusEnum] = mapped_column(
        default=StatusEnum.PUBLISHED,
        server_default=text("'DRAFT'")
    )
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id')) # Подключение к внешнему ключу таблицы users по полю id
    
    user: Mapped['User'] = relationship(
        'User',
        back_populates='posts',  # Устанавливаем связь с таблицей users через поле posts
    )
    
    # Вопрос: без разницы в каком классе устанавливать связующий ключ? ( устанавливать в классе, который больше зависит - (к большему))
    comment: Mapped['Comment'] = relationship( # здесь : или =? и я же могу назвать как захочу?
        'Comment',
        back_populates='posts',  # Здесь название атрибутка же другого класса как в строке 24? 
        cascade='all, delete-orphan', # указывет от главного? (от одного)
    )
    
    @classmethod
    @connection
    def create(cls,
               user_id:int,
               title: str,
               content:str,
               main_photo_url:str,
               photo_urls: list = [],
               session: Session = None) -> int:
        
        new_post = Post(
            user_id=user_id,
            title=title,
            content=content,
            main_photo_url=main_photo_url,
            photo_urls=photo_urls
        )
        
        session.add(new_post)
        session.commit()
        
        return new_post.id