from sqlalchemy.orm import Session
from models.enums import GenderEnum
from models.post import Post
from schemas import UserPydantic, UsernameIdPydantic
from settings.config import settings
from settings.database import Base
from models.user import User

def test_addition():
    u = User.add('John Doe','john.doe@example.com','password123', GenderEnum.MALE)
    u2 = User.add('Jane Doe','jane.doe@example.com','password456', GenderEnum.FEMALE)
    u3 = User.add('Alice Smith','alice.smith@example.com','password789', GenderEnum.FEMALE)
    return u, u2, u3


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
    # u, u2, u3 = test_addition()
    # print(u, type(u))
    # publish_post(30)
    # User.add_many(users_data)
    # u4 = User.get_per_username('username_5')
    # print(u4)
    # u5 = User.get_per_username('username_10')
    # print(u5)
    # all_users = User.get_all()
    # for user in all_users:
    #     # data = {'username': user.username, 'email': user.email, 'password': user.password, 'gender': user.profile.gender.value}
    #     # print(data)
    #     # print(user.to_dict())
    #     # print(user.profile)
    #     user_pydantic = UserPydantic.model_validate(user)
    #     print(user_pydantic)
    #     print(dict(user_pydantic))
    
    all_usernames_ids = User.get_all_username_id()
    
    for i in all_usernames_ids:
        # print(i)
        # data = {'user_id': i[0], 'username': i[1]} 
        # print(data)
        rez = UsernameIdPydantic.model_validate(i)
        print(dict(rez))



