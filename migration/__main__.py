import asyncio

from migration.legacy import Database as LegacyDatabase
from migration.legacy.schema import PreferencesSchema as LegacyPreferencesSchema
from migration.legacy.schema import SchoolInfoSchema as LegacySchoolInfoSchema
from migration.legacy.schema import UserSchema as LegacyUserSchema
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload

from crenata.infrastructure.sqlalchemy.preferences.domain.entity import (
    PreferencesSchema,
)
from crenata.infrastructure.sqlalchemy.schoolinfo.domain.entity import SchoolInfoSchema
from crenata.infrastructure.sqlalchemy.user.domain.entity import UserSchema


async def main():
    legacy = await LegacyDatabase.setup("기존 db url")
    legacy_session_maker = async_sessionmaker(
        legacy.engine, class_=AsyncSession, expire_on_commit=False
    )

    users: list[UserSchema] = []
    async with legacy_session_maker() as legacy_session:
        results = await legacy_session.execute(
            select(LegacyUserSchema).options(
                selectinload(
                    LegacyUserSchema.preferences.of_type(LegacyPreferencesSchema)
                ),
                selectinload(
                    LegacyUserSchema.school_info.of_type(LegacySchoolInfoSchema)
                ),
            )
        )
        for user in results.scalars().all():
            school_info_schema = None
            if user.school_info:
                school_info = user.school_info
                school_info_schema = SchoolInfoSchema(
                    discord_id=school_info.user_id,
                    name=school_info.school_name,
                    # idk why grade and room is str
                    grade=int(school_info.grade),
                    room=int(school_info.room),
                    edu_office_code=school_info.ATPT_OFCDC_SC_CODE,
                    standard_school_code=school_info.SD_SCHUL_CODE,
                    department=None,
                    major=None,
                )

            preferences_schema = PreferencesSchema(
                discord_id=user.preferences.user_id,
                private=user.preferences.private,
                ephemeral=user.preferences.ephemeral,
            )

            user_schema = UserSchema(
                discord_id=user.id,
                preferences=preferences_schema,
                school_info=school_info_schema,
            )
            users.append(user_schema)

    with open("migration.py", "w") as f:
        f.write(
            """
import asyncio
from crenata.infrastructure.sqlalchemy import Database
from crenata.infrastructure.sqlalchemy.preferences.domain.entity import (
    PreferencesSchema,
)
from crenata.infrastructure.sqlalchemy.schoolinfo.domain.entity import SchoolInfoSchema
from crenata.infrastructure.sqlalchemy.user.domain.entity import UserSchema

db_url = "마이그레이션할 db url"


"""
        )

        f.write(f"users = {users.__repr__()}")
        f.write("\n\n")
        f.write(
            """
async def main():
    database = await Database.setup(db_url)
    session_maker = database.session_maker

    async with session_maker() as session:
        session.add_all(users)
        await session.commit()

asyncio.run(main())
"""
        )


asyncio.run(main())
