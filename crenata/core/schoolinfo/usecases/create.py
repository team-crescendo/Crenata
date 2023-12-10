from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.schoolinfo.domain.repository import SchoolInfoRepository
from crenata.core.schoolinfo.exceptions import DuplicateSchoolInfo


class CreateSchoolInfoUseCase:
    def __init__(self, school_info_repository: SchoolInfoRepository) -> None:
        self.school_info_repository = school_info_repository

    async def execute(self, user_id: int, school_info: SchoolInfo) -> SchoolInfo:
        nullable_school_info = await self.school_info_repository.get_school_info(
            user_id
        )

        if not nullable_school_info:
            return await self.school_info_repository.create_school_info(
                user_id, school_info
            )

        raise DuplicateSchoolInfo
