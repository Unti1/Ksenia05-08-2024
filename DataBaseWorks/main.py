from sqlalchemy.orm import Session
from settings.config import settings
from settings.database import Base
from models.user import User

print(settings.DATABASE_NAME)

u = User.create_user('John Doe','john.doe@example.com','password123')
u2 = User.create_user('Jane Doe','jane.doe@example.com','password456')
u3 = User.create_user('Alice Smith','alice.smith@example.com','password789')
