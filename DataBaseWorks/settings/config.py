
import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_USER: str
    DATABASE_PASSWORD: str 
    DATABASE_NAME: str 
    DATABASE_SQLITE: str = ''
    
    # Other
    CREATOR_NAME: str
    
    model_config = SettingsConfigDict(
        env_file=os.path.join( os.path.dirname(os.path.abspath(__file__)), '.env'), 
        env_file_encoding='utf-8'
        )

settings = Settings()