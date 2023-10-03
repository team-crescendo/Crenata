from dataclasses import asdict

from sqlalchemy import select, update

from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.schoolinfo.domain.repository import SchoolInfoRepository
from crenata.infrastructure.sqlalchemy import Database
from crenata.infrastructure.sqlalchemy.schoolinfo.domain.entity import SchoolInfoSchema


class SchoolInfoRepositoryImpl(SchoolInfoRepository):
    def __init__(self, database: Database) -> None:
        self.database = database

    async def get_schoolinfo(self, user_id: int) -> SchoolInfo | None:
        async with self.database.session_maker() as session:
            async with session.begin():
                stmt = select(SchoolInfoSchema).where(
                    SchoolInfoSchema.discord_id == user_id
                )
                schoolinfo = await session.scalar(stmt)
                return schoolinfo.to_entity() if schoolinfo else None

    async def create_schoolinfo(
        self, user_id: int, schoolinfo: SchoolInfo
    ) -> SchoolInfo:
        async with self.database.session_maker() as session:
            async with session.begin():
                schoolinfo_schema = SchoolInfoSchema.from_entity(user_id, schoolinfo)
                session.add(schoolinfo_schema)
                return schoolinfo_schema.to_entity()

    async def update_schoolinfo(self, user_id: int, schoolinfo: SchoolInfo) -> None:
        async with self.database.session_maker() as session:
            async with session.begin():
                await session.execute(
                    update(SchoolInfoSchema).where(
                        SchoolInfoSchema.discord_id == user_id
                    ),
                    asdict(schoolinfo),
                )

    async def delete_schoolinfo(self, user_id: int) -> None:
        async with self.database.session_maker() as session:
            async with session.begin():
                await session.delete(SchoolInfoSchema.discord_id == user_id)
