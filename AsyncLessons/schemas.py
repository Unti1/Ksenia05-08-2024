from typing import List
from pydantic import BaseModel, ConfigDict

from models.enums import GenderEnum, ProfessionEnum


class ProfilePydantic(BaseModel):
    name: str
    surname: str|None
    age: int|None
    gender: GenderEnum
    profession: ProfessionEnum
    interests: List[str]|None
    contacts: dict|None
    
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

class UserPydantic(BaseModel):
    username: str
    email: str
    password: str
    profile: ProfilePydantic|None
    
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

class UsernameIdPydantic(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)