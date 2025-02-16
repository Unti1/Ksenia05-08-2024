import pytest

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


@pytest.fixture(scope='module')
def user():
    """Фикстура для создания пользователя."""
    return User(
        username="testuser", 
        password="password123"
        )