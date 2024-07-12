import data
from database.models import Base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine(data.DB_LITE, echo=True)
session_marker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

from contextlib import asynccontextmanager


@asynccontextmanager
async def get_session():
    async with session_marker() as session:
        try:
            yield session
        finally:
            await session.close()


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
