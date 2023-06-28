from crenata.core.user.domain.entity import User
from crenata.core.user.domain.repository import UserRepository
from crenata.core.user.exceptions import UserNotFound


class GetUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> User:
        user = await self.user_repository.get_user(user_id)
        if not user:
            raise UserNotFound
        return user
