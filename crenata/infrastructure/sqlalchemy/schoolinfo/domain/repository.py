from dataclasses import asdict

from sqlalchemy import select, update

from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.schoolinfo.domain.repository import SchoolInfoRepository
from crenata.infrastructure.sqlalchemy import Database
from crenata.infrastructure.sqlalchemy.schoolinfo.domain.entity import SchoolInfoSchema


class SchoolInfoRepositoryImpl(SchoolInfoRepository):
    def __init__(self, database: Database) -> None:
        self.database = database

    async def get_school_info(self, user_id: int) -> SchoolInfo | None:
        async with self.database.session_maker() as session:
            async with session.begin():
                stmt = select(SchoolInfoSchema).where(
                    SchoolInfoSchema.discord_id == user_id
                )
                school_info = await session.scalar(stmt)
                return school_info.to_entity() if school_info else None

    async def create_school_info(
        self, user_id: int, school_info: SchoolInfo
    ) -> SchoolInfo:
        async with self.database.session_maker() as session:
            async with session.begin():
                school_info_schema = SchoolInfoSchema.from_entity(user_id, school_info)
                session.add(school_info_schema)
                return school_info_schema.to_entity()

    async def update_school_info(self, user_id: int, school_info: SchoolInfo) -> None:
        async with self.database.session_maker() as session:
            async with session.begin():
                await session.execute(
                    update(SchoolInfoSchema).where(
                        SchoolInfoSchema.discord_id == user_id
                    ),
                    asdict(school_info),
                )

    async def delete_school_info(self, user_id: int) -> None:
        async with self.database.session_maker() as session:
            async with session.begin():
                await session.delete(SchoolInfoSchema.discord_id == user_id)
