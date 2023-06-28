from crenata.core.user.domain.repository import UserRepository


class DeleteUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> None:
        await self.user_repository.delete_user(user_id)
