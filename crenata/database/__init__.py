from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine
from sqlalchemy.orm import relationship

from crenata.database.registry import mapper_registry
from crenata.database.schema import *
from crenata.database.table import *
from crenata.typing import DatabaseMapping


class Database:
    """
    이 클래스는 데이터베이스를 설정하고, 엔진을 생성합니다.

    직접적으로 사용해서는 안됩니다.
    """

    mapping: DatabaseMapping = [
        (
            UserSchema,
            user_table,
            {
                "school_info": relationship(
                    SchoolInfoSchema,
                    uselist=False,
                    cascade="all, delete",
                    passive_deletes=True,
                ),
                "preferences": relationship(
                    PreferencesSchema,
                    uselist=False,
                    cascade="all, delete",
                    passive_deletes=True,
                ),
            },
        ),
        (SchoolInfoSchema, schoolinfo_table, {}),
        (PreferencesSchema, preferences_table, {}),
    ]

    def __init__(self, engine: AsyncEngine) -> None:
        self.engine = engine

    @classmethod
    async def setup(cls, db_url: str) -> "Database":
        """
        데이터베이스를 설정합니다.

        스키마와 테이블을 매핑하고 엔진을 생성합니다.
        """
        for domain, table, properties in cls.mapping:
            mapper_registry.map_imperatively(domain, table, properties=properties)
        engine = create_async_engine(db_url)
        async with engine.begin() as connection:
            await connection.run_sync(
                mapper_registry.metadata.create_all, checkfirst=True
            )
        return cls(engine)
