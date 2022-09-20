import sqlalchemy as sa
from database import Base

import enum


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

#users = sqlalchemy.Table(
#    "users",
#    metadata,
#    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#    sqlalchemy.Column("email", sqlalchemy.String(40), unique=True, index=True),
#    sqlalchemy.Column("name", sqlalchemy.String(100)),
#    sqlalchemy.Column("role", sqlalchemy.Enum(UserRoles)),
#    sqlalchemy.Column("hashed_password", sqlalchemy.String()),
#)
