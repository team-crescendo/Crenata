from abc import ABC
from typing import Optional

from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.user.domain.entity import User


class UserRepository(ABC):
    async def get_user(self, user_id: int) -> Optional[User]:
        ...

    async def create_user(self, user: User) -> User:
        ...

    async def update_user(self, user: User) -> User:
        ...

    async def delete_user(self, user_id: int) -> None:
        ...

    async def get_all_same_school_users(self, school_info: SchoolInfo) -> list[User]:
        ...
