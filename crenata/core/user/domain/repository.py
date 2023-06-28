from abc import ABC
from typing import Optional

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
