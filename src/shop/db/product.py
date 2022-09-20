import sqlalchemy as sa
from database import Base


class Product(Base):
    __tablename__ = 'products'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text)
    author = sa.Column(sa.Text)
    description = sa.Column(sa.Text)
    image = sa.Column(sa.Text)
    price = sa.Column(sa.Float)
    category_id = sa.Column(sa.Integer, sa.ForeignKey('categories.id'))
