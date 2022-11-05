from abc import ABC, abstractmethod
from typing import Optional

from crenata.domain.user import User


class AbstractDatabase(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> None:
        ...

    @abstractmethod
    async def get_user(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    async def remove_user(self, user: User) -> None:
        ...
