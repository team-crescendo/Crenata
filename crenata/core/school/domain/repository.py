from abc import ABC, abstractmethod

from crenata.core.school.domain.entity import School


class SchoolRepository(ABC):
    @abstractmethod
    async def search_school(self, school_name: str) -> list[School] | None:
        ...
