import platform
import pytest
import sys

def some_cross_platform_function():
    return "Success"

def some_linux_function():
    return "Linux"
    
@pytest.mark.skipif('linux' not in platform.architecture()[1].lower(),
                    reason="Тест не поддерживается на Windows, так как работает только для Linux")
def test_linux_only_functionality():
    assert some_linux_function()

@pytest.mark.skip(reason='Пока не хочу выполнять')
def test_cross_platform_functionality():
    assert some_cross_platform_function() == "Success"

print(platform.architecture())
print(some_linux_function())