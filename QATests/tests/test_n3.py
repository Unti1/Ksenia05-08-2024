import pytest
# from tests.test_n2 import user
from fixes import user # Фикстры мы берем из конкретных файлов

def test_existing_user_fixture(user):
    """Проверяем, что фикстра user возвращает существующего пользователя."""
    assert user