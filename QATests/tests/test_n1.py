import pytest

def apply_discount(price, discount):
    """Простая функция для вычисления цены после скидки."""
    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount / 100)

# @pytest.mark.parametrize("price, discount, expected", [
#                             (100, 10, 90),
#                             (200, 50, 100),
#                             (50, 0, 50),
#                             (100, -100, 0),
#                             (100, 100, 0),
#                             ])
# def test_apply_discount(price, discount, expected):
#     """Тест для функции apply_discount."""
#     assert apply_discount(price, discount) == expected


# @pytest.mark.parametrize("price, discount", 
#                          [
#                             (100, 110),
#                             (100, -100),
#                             (100, 0),
#                             (100, 200),
#                              ])
# # Тест на случай, когда скидка превышает допустимый диапазон
# def test_apply_discount_invalid(price, discount):
#     with pytest.raises(ValueError):
#         apply_discount(price, discount)
