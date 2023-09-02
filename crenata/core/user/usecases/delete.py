from crenata.core.user.domain.repository import UserRepository
from crenata.core.user.exceptions import UserNotFound


class DeleteUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> None:
        user = await self.user_repository.get_user(user_id)
        if user is None:
            raise UserNotFound
        await self.user_repository.delete_user(user_id)
