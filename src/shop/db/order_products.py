import sqlalchemy as sa
from database import Base


class OrderProducts(Base):
    __tablename__ = 'order_products'

    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.id'), primary_key=True)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.id'), primary_key=True)
    amount = sa.Column(sa.Integer, nullable=False)
