import sqlalchemy as sa
import enum
from database import Base


class OrderStatus(enum.Enum):
    CREATED = 'created'
    PLACED = 'placed'
    PAID = 'paid'
    DELIVERED = 'delivered'


class Order(Base):
    __tablename__ = 'orders'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    sum = sa.Column(sa.Float)
    status = sa.Column(sa.Enum(OrderStatus))
