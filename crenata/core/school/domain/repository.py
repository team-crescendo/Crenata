from abc import ABC, abstractmethod
from typing import Optional

from crenata.core.school.domain.entity import School


class SchoolRepository(ABC):
    @abstractmethod
    async def search_school(self, school_name: str) -> Optional[list[School]]:
        ...
