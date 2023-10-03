from dataclasses import asdict

from sqlalchemy import select, update

from crenata.core.preferences.domain.entity import Preferences
from crenata.core.preferences.domain.repository import PreferencesRepository
from crenata.infrastructure.sqlalchemy import Database
from crenata.infrastructure.sqlalchemy.preferences.domain.entity import (
    PreferencesSchema,
)


class PreferencesRepositoryImpl(PreferencesRepository):
    def __init__(self, database: Database) -> None:
        self.database = database

    async def get_preferences(self, user_id: int) -> Preferences:
        async with self.database.session_maker() as session:
            async with session.begin():
                stmt = select(PreferencesSchema).where(
                    PreferencesSchema.discord_id == user_id
                )
                preferences = await session.scalar(stmt)
                assert preferences is not None
                return preferences.to_entity()

    async def update_preferences(self, user_id: int, preferences: Preferences) -> None:
        async with self.database.session_maker() as session:
            async with session.begin():
                await session.execute(
                    update(PreferencesSchema).where(
                        PreferencesSchema.discord_id == user_id
                    ),
                    asdict(preferences),
                )
