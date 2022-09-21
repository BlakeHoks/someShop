import sqlalchemy as sa
from database import Base

import enum
# TODO: сделать роли


class UserRoles(enum.Enum):
    ADMIN = 'admin'
    USER = 'user'


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text, unique=True)
    username = sa.Column(sa.Text, unique=True)
    #role = sa.Column(sa.Enum(UserRoles))
    password_hash = sa.Column(sa.Text)
