from crenata.core.majorinfo.domain.entity import MajorInfo
from crenata.core.majorinfo.domain.repository import MajorInfoRepository
from crenata.core.majorinfo.exceptions import MajorInfoNotFound


class GetMajorInfoUseCase:
    def __init__(self, majorinfo_repository: MajorInfoRepository) -> None:
        self.majorinfo_repository = majorinfo_repository

    async def execute(
        self, edu_office_code: str, standard_school_code: str
    ) -> list[MajorInfo]:
        nullable_majorinfo = await self.majorinfo_repository.get_majorinfo(
            edu_office_code, standard_school_code
        )

        if not nullable_majorinfo:
            raise MajorInfoNotFound

        return nullable_majorinfo
