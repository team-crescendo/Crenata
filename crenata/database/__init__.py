from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine

from crenata.database.base import Base
from crenata.database.schema import *


class Database:
    """
    이 클래스는 데이터베이스를 설정하고, 엔진을 생성합니다.

    직접적으로 사용해서는 안됩니다.
    """

    def __init__(self, engine: AsyncEngine) -> None:
        self.engine = engine

    @classmethod
    async def setup(cls, db_url: str) -> "Database":
        """
        데이터베이스를 설정합니다.

        스키마와 테이블을 매핑하고 엔진을 생성합니다.
        """
        engine = create_async_engine(db_url)
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all, checkfirst=True)
        return cls(engine)
