from sqlalchemy import Table
from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine

from crenata.abc.domain import AbstractDomain
from crenata.database.registry import mapper_registry
from crenata.database.table import *
from crenata.domain.entities.user import User


class ORM:
    mapping: list[tuple[type[AbstractDomain], Table]] = [(User, user_table)]

    def __init__(self, engine: AsyncEngine) -> None:
        self.engine = engine

    @classmethod
    def override_mapping(cls, domain: type[AbstractDomain], table: Table):
        for i, mapping in enumerate(cls.mapping):
            default_domain, _ = mapping
            if issubclass(domain, default_domain):
                cls.mapping[i] = (domain, table)

    @classmethod
    async def setup(cls, db_url: str) -> "ORM":
        for domain, table in cls.mapping:
            mapper_registry.map_imperatively(domain, table)
        engine = create_async_engine(db_url)
        async with engine.begin() as connection:
            await connection.run_sync(
                mapper_registry.metadata.create_all, checkfirst=True
            )
        return cls(engine)
