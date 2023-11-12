from crenata.core.schoolinfo.domain.repository import SchoolInfoRepository
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound


class DeleteSchoolInfoUseCase:
    def __init__(self, schoolinfo_repository: SchoolInfoRepository) -> None:
        self.schoolinfo_repository = schoolinfo_repository

    async def execute(self, user_id: int) -> None:
        nullable_schoolinfo = await self.schoolinfo_repository.get_schoolinfo(user_id)

        if nullable_schoolinfo is None:
            raise SchoolInfoNotFound

        await self.schoolinfo_repository.delete_schoolinfo(user_id)
