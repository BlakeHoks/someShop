from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

from src.shop.settings import settings

Base = declarative_base()
metadata = MetaData()


engine = create_engine(
    settings.database_url,
)


Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
