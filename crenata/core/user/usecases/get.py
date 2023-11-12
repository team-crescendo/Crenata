from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound
from crenata.core.user.domain.entity import User
from crenata.core.user.domain.repository import UserRepository
from crenata.core.user.exceptions import UserNotFound


class GetUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> User:
        user = await self.user_repository.get_user(user_id)

        if user is None:
            raise UserNotFound
        if user.school_info is None:
            raise SchoolInfoNotFound
        return user


class GetAllSameSchoolUsersUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self, school_info: SchoolInfo) -> list[User]:
        users = await self.user_repository.get_all_same_school_users(school_info)
        return users
