from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine

from crenata.database.registry import mapper_registry
from crenata.database.table import *
from crenata.domain.entities.user import User

mapper_registry.map_imperatively(User, user_table)


class ORM:
    def __init__(self, engine: AsyncEngine) -> None:
        self.engine = engine

    @classmethod
    async def setup(cls, db_url: str) -> "ORM":
        engine = create_async_engine(db_url)
        async with engine.begin() as connection:
            await connection.run_sync(
                mapper_registry.metadata.create_all, checkfirst=True
            )
        return cls(engine)


