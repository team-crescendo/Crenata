from dataclasses import asdict
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from crenata.database import Database
from crenata.database.schema import SchoolInfoSchema


class SchoolInfoRepository:
    """
    학교 정보 레포지토리입니다.


    """

    def __init__(self, database: Database) -> None:
        self.database = database

    async def create(self, school_info: SchoolInfoSchema) -> None:
        """
        학교 정보를 생성합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                return session.add(school_info)

    async def update(
        self, update_school_info: SchoolInfoSchema
    ) -> Optional[SchoolInfoSchema]:
        """
        학교 정보를 업데이트합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                school_info = await session.get(SchoolInfoSchema, update_school_info.id)
                if school_info:
                    for key, value in asdict(update_school_info).items():
                        setattr(school_info, key, value)
                    return school_info

        return None

    async def read(self, user_id: int) -> Optional[SchoolInfoSchema]:
        """
        학교 정보를 읽어옵니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                stmt = select(SchoolInfoSchema).where(
                    SchoolInfoSchema.user_id == user_id
                )
                return (await session.execute(stmt)).scalar_one_or_none()

    async def delete(self, school_info: SchoolInfoSchema) -> None:
        """
        학교 정보를 삭제합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                return await session.delete(school_info)
