from dataclasses import asdict
from typing import Optional

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload

from crenata.abc.domain import AbstractDomain
from crenata.database import Database
from crenata.database.schema import UserSchema


class UserRepository:
    """
    유저 레포지토리입니다.

    유저를 생성, 읽기, 업데이트, 삭제합니다.
    """

    def __init__(self, database: Database) -> None:
        self.database = database

    async def create(self, user: UserSchema) -> None:
        """
        유저를 생성합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                return session.add(user)

    async def update(self, update_user: UserSchema) -> Optional[UserSchema]:
        """
        유저를 업데이트합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                user = await session.get(UserSchema, update_user.id)
                if user:
                    user.preferences = update_user.preferences
                    user.school_info = update_user.school_info
                    return user

        return None

    async def read(self, user_id: int) -> Optional[UserSchema]:
        """
        유저를 읽어옵니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                return await session.get(
                    UserSchema,
                    user_id,
                    [
                        selectinload(UserSchema.preferences),
                        selectinload(UserSchema.school_info),
                    ],
                )

    async def delete(self, user: UserSchema) -> None:
        """
        유저를 삭제합니다.
        """
        async with AsyncSession(
            self.database.engine, expire_on_commit=False
        ) as session:
            async with session.begin():
                await session.delete(user)
        return None
