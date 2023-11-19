from dataclasses import asdict
from typing import Optional

from migration.legacy import Database
from migration.legacy.schema import PreferencesSchema
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession


class PreferencesRepository:
    """
    환경설정 레포지토리입니다.

    환경설정을 생성, 읽기, 업데이트, 삭제합니다.
    """

    def __init__(self, database: Database) -> None:
        self.database = database

    async def create(self, preferences_info: PreferencesSchema) -> None:
        """
        환경설정을 생성합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                return session.add(preferences_info)

    async def update(
        self, update_preferences_info: PreferencesSchema
    ) -> Optional[PreferencesSchema]:
        """
        환경설정을 업데이트합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                preferences_info = await session.get(
                    PreferencesSchema, update_preferences_info.id
                )
                if preferences_info:
                    for key, value in asdict(update_preferences_info).items():
                        setattr(preferences_info, key, value)
                    return preferences_info

        return None

    async def read(self, user_id: int) -> Optional[PreferencesSchema]:
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            """
            환경설정을 읽어옵니다.
            """
            async with session.begin():
                stmt = select(PreferencesSchema).where(
                    PreferencesSchema.user_id == user_id
                )
                return (await session.execute(stmt)).scalar_one_or_none()

    async def delete(self, preferences_info: PreferencesSchema) -> None:
        """
        환경설정을 삭제합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                return await session.delete(preferences_info)
