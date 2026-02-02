from app.config import DataBaseConfig
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()

async_engine = create_async_engine(
    DataBaseConfig.SQLALCHEMY_DATABASE_URI,
    echo=True,
    poolclass=NullPool,
    future=True
)

async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

sync_db_url = DataBaseConfig.SQLALCHEMY_DATABASE_URI.replace(
    "postgresql+asyncpg://", "postgresql+psycopg2://"
)
sync_engine = create_engine(sync_db_url)
SyncSession = sessionmaker(bind=sync_engine)
