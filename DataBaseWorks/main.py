from sqlalchemy.orm import Session
from models.enums import GenderEnum
from models.post import Post
from settings.config import settings
from settings.database import Base
from models.user import User

print(settings.DATABASE_NAME)

u = User.create_user('John Doe','john.doe@example.com','password123', GenderEnum.MALE)
u2 = User.create_user('Jane Doe','jane.doe@example.com','password456', GenderEnum.FEMALE)
u3 = User.create_user('Alice Smith','alice.smith@example.com','password789', GenderEnum.FEMALE)

print(u)

def publish_post(u_id):
    u = User.get_by_id(u_id)
    if u:
        Post.create(user_id=u.id, 
                    title='New Post', 
                    content='This is a new post.', 
                    main_photo_url='https://example.com/photo.jpg')
        print(f"Post published by {u.username}")
    else:
        print("User not found")

if __name__ == '__main__':
    publish_post(17)

