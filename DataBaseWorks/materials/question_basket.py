


from sqlalchemy import ForeignKey, select
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship
from settings.database import Base, connection

# 2 способ реализации корзины и продуктов

# [
#     {"product_id": 1, "quantity": 2},
#     {"product_id": 2, "quantity": 1}
# ]

class Basket(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    items: Mapped[dict] = mapped_column(JSON, default=[])

    
    user: Mapped['User'] = relationship(
        'User',
        back_populates='baskets',
        uselist=False
        )
    
    @classmethod
    @connection
    def add_item(cls, basket_id, product_id, quantity, session: Session = None):
        rows = session.execute(select(cls).where(cls.id == basket_id))
        basket = rows.scalars().first()
        if not basket:
            return False, 'Корзины не существует'
        
        for items in basket.items:
            if items['product_id'] == product_id:
                items['quantity'] += quantity
                session.commit()
                return True, 'Товар добавлен в корзину'
        items.append({'product_id': product_id, 'quantity': quantity})
        session.commit()
        return True, 'Товар добавлен в корзину'


# 1 способ реализации корзины и продуктов

        
class Product(Base):
    title: Mapped[str]
    description: Mapped[str]
    price: Mapped[float] = mapped_column(default=0.0)
    
    basket_items = relationship(
        'BasketItem', 
        back_populates='product',
        cascade='all, delete-orphan'
        )



class Basket(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    items: Mapped['BasketItem'] = relationship(
        'BasketItem',
        back_populates='basket',
        cascade='all, delete-orphan',
        lazy = 'joined'
    )

class BasketItem(Base):
    basket_id: Mapped[int] = mapped_column(ForeignKey('baskets.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    quantity: Mapped[int] = mapped_column(default=1)
    
    basket: Mapped['Basket'] = relationship(
        'Basket',
        back_populates='items'
    )
    
    product: Mapped['Product'] = relationship(
        'Product',
        back_populates='basket_items',
        lazy='joined'
        )

# Пример:

if __name__ == '__main__':
    prod1 = Product.add(title="Laptop", price=900, description="High-performance laptop")
    prod2 = Product.add(title="Smartphone", price=500, description="Latest smartphone")
    prod3 = Product.add(title="Tablet", price=300, description="Portable tablet")

    basket = Basket.add(user_id=1)
    
    basket_item1 = BasketItem.add(basket_id=basket.id, product_id=prod1.id) # добавляем 1 товар в корзину
    basket_item2 = BasketItem.add(basket_id=basket.id, product_id=prod2.id) # добавляем 2 товар в корзину

    BasketItem.delete_per_id(basket_item1.id) # удаляем 1 товар из корзины
    
    # преимущество этого метода в том что дополнительно не нужно определять новые методы для работы с таблицей товаров
    # а достаточно уже реализованных в Base методах
    
    



