
import os
import pathlib
from pydantic_settings import BaseSettings, SettingsConfigDict  


class Settings(BaseSettings):
    # Database
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_USER: str
    DATABASE_PASSWORD: str 
    DATABASE_NAME: str
    DATABASE_SQLITE: str = 'sqlite:///db.sqlite3'
    DATABASE_ASYNC_SQLITE: str = 'sqlite+aiosqlite:///db.sqlite3'
    
    TG_API: str
    
    ROOT_PATH: pathlib.Path = pathlib.Path(__file__).parent.parent  
    
    # Other
    CREATOR_NAME: str
    
    model_config = SettingsConfigDict(
        env_file = ROOT_PATH / '.env',
        env_file_encoding='utf-8'
        )
    
    def get_db_url(self):
        return (f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}")
    
    def get_async_db_url(self):
        return (f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}")

settings = Settings()