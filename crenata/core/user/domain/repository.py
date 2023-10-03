from abc import ABC, abstractmethod
from typing import Optional

from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.user.domain.entity import User


class UserRepository(ABC):
    @abstractmethod
    async def get_user(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    async def create_user(self, user: User) -> User:
        ...

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        ...

    @abstractmethod
    async def get_all_same_school_users(self, school_info: SchoolInfo) -> list[User]:
        ...
