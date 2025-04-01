from typing import Any, Dict, List, Self

import bcrypt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, relationship

from models.enums import GenderEnum, ProfessionEnum
from models.profile import Profile
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
    
    
    @classmethod
    @connection
    async def add(cls, 
            username: str, 
            email: str, 
            password: str,
            gender: GenderEnum,
            name: str = None,
            surname: str = None,
            age: int = None,
            profession: ProfessionEnum = ProfessionEnum.UNEMPLOYED,
            interests: list[str] = [],
            contacts: dict = {},
            session: AsyncSession = None) -> dict[str, int]:
        """Этот метод создает нового пользователя в базе данных.

        Args:
            username (str): имя пользователя
            email (str): электронная почта пользователя
            password (str): пароль пользователя
            session (AsyncSession, optional): db session. Defaults to None.

        Returns:
            User: новый созданный пользователь

        """
        existed_row = await session.execute(select(cls).where(cls.username == username))
        user = existed_row.scalars().first() 
        if user:
            return user

        
        hash_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username=username, email=email, password=str(hash_pw)[2:-1])
    
        session.add(new_user)
        session.flush() # Промежуточный шаг для получения user.id без коммита
    
        profile = Profile(
            user_id = new_user.id,
            name=name if name else username,
            surname=surname,
            age=age,
            gender=gender,
            profession=profession,
            interests=interests,
            contacts=contacts,
        )
    
        session.add(profile)
        session.commit()
        print(f'Создан пользователь с ID {new_user.id}и ему присвоен профиль с ID {profile.id}')

        return {'user_id': new_user.id, 'profile_id': profile.id}

    @classmethod
    @connection
    async def add_many(cls,
                users_data: List[Dict[str, Any]], 
                session: AsyncSession = None) -> list[int]:
        
        users_list = [
            User(
                username=user_data['username'],
                email=user_data['email'],
                password=str(bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt()))[2:-1],

            )   
            for user_data in users_data
        ]
        
        session.add_all(users_list)
        await session.flush()
        
        profile_list = [
            Profile(
                user_id=user_row.id,
                name=user_row.username,
                gender= GenderEnum.MALE,
                interests= [],
                contacts={},
            )   
            for user_row in users_list
        ]
        
        session.add_all(profile_list)
        await session.commit()

    @classmethod
    @connection
    async def get_per_username(cls,
                         username:str,
                         session: AsyncSession = None) -> Self|None:
        rows = await session.execute(select(cls).where(cls.username == username))
        user = rows.scalars().first()
        return user

    @classmethod
    @connection
    async def get_all_username_id(cls, session: AsyncSession = None):
        rows = await session.execute(select(cls.id, cls.username))
        users = rows.all()
        return users

    @classmethod
    @connection
    async def get_user_i(cls, user_id: int, session: AsyncSession = None):
        query = select(cls).filter_by(id=user_id)
        # query = select(cls).filter_by(cls.id==user_id)
        # query = select(cls).where(cls.id==user_id)
        result = await session.execute(query)
        user_info = result.scalar_one_or_none()
        return user_info


    def __str__(self):
        return f'[{self.id}] {self.username} | {self.email}'
