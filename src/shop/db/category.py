import sqlalchemy as sa
from database import Base


class Category(Base):
    __tablename__ = 'categories'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text)
