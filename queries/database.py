import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

from sqlalchemy import create_engine, text, async_sessionmaker, create_async_engine

DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME = os.getenv('DB_USER'), os.getenv('DB_PASS'), os.getenv(
    'DB_HOST'), os.getenv('DB_PORT'), os.getenv('DB_NAME')

sync_engine = create_engine(  # Создание синхронного движка
    url=f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",  # DSN
    echo=True,
)

async_engine = create_async_engine(
    url=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=False,
)

session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
