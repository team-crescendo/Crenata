from crenata.core.school.domain.entity import School
from crenata.core.school.domain.repository import SchoolRepository
from crenata.core.school.exception import SchoolNotFound


class GetSchoolUseCase:
    def __init__(self, school_repository: SchoolRepository) -> None:
        self.school_repository = school_repository

    async def execute(self, school_name: str) -> list[School]:
        schools = await self.school_repository.search_school(school_name)

        if schools is None:
            raise SchoolNotFound

        return schools
