from typing import Optional

from sqlalchemy.ext.asyncio.session import AsyncSession

from crenata.abc.usecase.user import AbstractDAOUser
from crenata.database import ORM
from crenata.domain.entities.user import User


class DAOUser(AbstractDAOUser):
    def __init__(self, orm: ORM) -> None:
        self.orm = orm

    async def create(self, user: User) -> None:
        async with AsyncSession(self.orm.engine, expire_on_commit=False) as session:
            async with session.begin():
                return session.add(user)

    async def get(self, user_id: int) -> Optional[User]:
        async with AsyncSession(self.orm.engine, expire_on_commit=False) as session:
            async with session.begin():
                return await session.get(User, user_id)

    async def remove(self, user: User) -> None:
        async with AsyncSession(self.orm.engine, expire_on_commit=False) as session:
            async with session.begin():
                return await session.delete(user)
