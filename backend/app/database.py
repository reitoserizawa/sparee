from app.config import DataBaseConfig
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()

async_engine = create_async_engine(
    DataBaseConfig.SQLALCHEMY_DATABASE_URI,
    echo=True,
    future=True
)

async_session = async_sessionmaker(
    engine=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
