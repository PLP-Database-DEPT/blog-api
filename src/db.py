from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine 
from .config import settings
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator 

engine: AsyncEngine = create_async_engine(
    url=settings.DB_URL,
    echo=True 
)

async_session=sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False 
)

async def get_session()-> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session: 
        yield session 


async def initdb() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
