import pytest

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

@pytest.fixture(scope='package')
def user():
    """Фикстура для создания пользователя."""
    return User(
        username="testuser", 
        password="password123"
        )


def test_user_creation(user):
    assert user.username == "testuser"
    assert user.password == "password123"

# def test_user_password_change(user):
#     user.password = 'newpassword456'
#     assert user.password == 'newpassword456'

# def test_user_after_change_pass(user):
#     assert user.password == "newpassword456"
