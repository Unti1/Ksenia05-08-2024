from sqlalchemy.orm import Session
from models.enums import GenderEnum
from models.post import Post
from settings.config import settings
from settings.database import Base
from models.user import User

print(settings.DATABASE_NAME)

u = User.add('John Doe','john.doe@example.com','password123', GenderEnum.MALE)
u2 = User.add('Jane Doe','jane.doe@example.com','password456', GenderEnum.FEMALE)
u3 = User.add('Alice Smith','alice.smith@example.com','password789', GenderEnum.FEMALE)

print(u)

def publish_post(u_id):
    u = User.get_by_id(u_id)
    if u:
        Post.add(user_id=u.id, 
                    title='New Post', 
                    content='This is a new post.',
                    main_photo_url='https://example.com/photo.jpg')
        print(f"Post published by {u.username}")
    else:
        print("User not found")

users_data = [
    {'username': f'username_{x}', 
     'email': f'username{x}@example.com', 
     'password': 'password123', 
     'gender': GenderEnum.MALE} for x in range(10)
]


if __name__ == '__main__':
    # publish_post(u.id)
    # User.add_many(users_data)
    u4 = User.get_per_username('username_5')
    print(u4)
    u5 = User.get_per_username('username_10')
    print(u5)


