from abc import ABC

from crenata.core.school.domain.entity import School


class SchoolRepository(ABC):
    async def search_school(self, school_name: str) -> list[School]:
        ...
