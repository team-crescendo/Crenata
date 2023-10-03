from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.schoolinfo.domain.repository import SchoolInfoRepository
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound


class GetSchoolInfoUseCase:
    def __init__(self, schoolinfo_repository: SchoolInfoRepository) -> None:
        self.schoolinfo_repository = schoolinfo_repository

    async def execute(self, user_id: int) -> SchoolInfo:
        getted_schoolinfo = await self.schoolinfo_repository.get_schoolinfo(user_id)

        if getted_schoolinfo is None:
            raise SchoolInfoNotFound

        return getted_schoolinfo
