import sys
from typing import AsyncGenerator, Annotated, Tuple

from fastapi import Depends
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession

from app.core.settings import settings


def create_database_uri(db_type: str = 'postgres') -> URL:
    uri = URL.create(
        drivername=settings.DB_DRIVERNAME if db_type == settings.DB_DRIVERNAME else 'mysql+asyncmy',
        username=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
    )
    return uri


def create_async_engine_and_session(url: str | URL) -> Tuple[AsyncEngine, async_sessionmaker[AsyncSession]]:
    try:
        engine = create_async_engine(
            url,
            echo=settings.DB_ECHO,
            echo_pool=settings.DB_ECHO_POOL,
            future=settings.DB_FUTURE,
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_MAX_OVERFLOW,
            pool_timeout=settings.DB_POOL_TIMEOUT,
            pool_recycle=settings.DB_POOL_RECYCLE,
            pool_pre_ping=settings.DB_POOL_PRE_PING,
            pool_use_lifo=settings.DB_POOL_USE_INFO)
    except Exception as e:
        sys.exit()
    else:
        db_session = async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            autoflush=False,
            expire_on_commit=False,
        )
        return engine, db_session


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_db_session() as session:
        yield session


DATABASE_URI = create_database_uri()

async_engine, async_db_session = create_async_engine_and_session(DATABASE_URI)

CurrentSession = Annotated[AsyncSession, Depends(get_db)]
