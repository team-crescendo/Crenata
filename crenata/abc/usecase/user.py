from abc import ABC, abstractmethod
from typing import Optional

from crenata.domain.entities.user import User


class AbstractDAOUser(ABC):
    @abstractmethod
    async def create(self, user: User) -> None:
        ...

    @abstractmethod
    async def get(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    async def remove(self, user: User) -> None:
        ...
