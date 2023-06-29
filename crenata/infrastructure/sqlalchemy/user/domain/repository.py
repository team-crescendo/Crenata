from sqlalchemy.sql import select

from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.user.domain.entity import User
from crenata.core.user.domain.repository import UserRepository
from crenata.infrastructure.sqlalchemy import Database
from crenata.infrastructure.sqlalchemy.schoolinfo.domain.entity import SchoolInfoSchema
from crenata.infrastructure.sqlalchemy.user.domain.entity import UserSchema


class UserRepositoryImpl(UserRepository):
    def __init__(self, database: Database) -> None:
        self.database = database

    async def get_user(self, user_id: int) -> User | None:
        async with self.database.session() as session:
            async with session.begin():
                user = await session.get(UserSchema, user_id)
                return user.to_entity() if user else None

    async def create_user(self, user: User) -> User:
        async with self.database.session() as session:
            async with session.begin():
                user_schema = UserSchema.from_entity(user)
                session.add(user_schema)
                return user_schema.to_entity()

    async def update_user(self, user: User) -> User:
        async with self.database.session() as session:
            async with session.begin():
                user_schema = UserSchema.from_entity(user)
                await session.merge(user_schema)
                return user_schema.to_entity()

    async def delete_user(self, user_id: int) -> None:
        async with self.database.session() as session:
            async with session.begin():
                await session.delete(UserSchema.discord_id == user_id)

    async def get_all_same_school_users(self, school_info: SchoolInfo) -> list[User]:
        async with self.database.session() as session:
            async with session.begin():
                query = (
                    select(UserSchema)
                    .join(SchoolInfoSchema)
                    .where(
                        SchoolInfoSchema.ATPT_OFCDC_SC_CODE
                        == school_info.ATPT_OFCDC_SC_CODE,
                        SchoolInfoSchema.SD_SCHUL_CODE == school_info.SD_SCHUL_CODE,
                    )
                )
                users = await session.execute(query)
                return [user.to_entity() for user in users.scalars().all()]
