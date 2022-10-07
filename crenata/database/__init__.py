from typing import Optional

from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from crenata.database.registry import mapper_registry
from crenata.database.table import *
from crenata.domain.user import User


class ORM:
    def __init__(self, engine: AsyncEngine) -> None:
        self.engine = engine

    @classmethod
    async def setup(cls, db_url: str) -> "ORM":
        mapper_registry.map_imperatively(User, user_table)
        engine = create_async_engine(db_url)
        async with engine.begin() as connection:
            await connection.run_sync(
                mapper_registry.metadata.create_all, checkfirst=True
            )
        return cls(engine)

    async def create_user(self, user: User) -> None:
        async with AsyncSession(self.engine, expire_on_commit=False) as session:
            async with session.begin():
                return session.add(user)

    async def get_user(self, user_id: int) -> Optional[User]:
        async with AsyncSession(self.engine, expire_on_commit=False) as session:
            async with session.begin():
                return await session.get(User, user_id)

    async def remove_user(self, user: User) -> None:
        async with AsyncSession(self.engine, expire_on_commit=False) as session:
            async with session.begin():
                return await session.delete(user)
