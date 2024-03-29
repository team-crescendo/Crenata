from crenata.core.user.domain.entity import User
from crenata.core.user.domain.repository import UserRepository
from crenata.core.user.exceptions import DuplicateUser


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, user: User) -> User:
        nullable_user = await self.user_repository.get_user(user.discord_id)

        if nullable_user is None:
            return await self.user_repository.create_user(user)

        raise DuplicateUser
