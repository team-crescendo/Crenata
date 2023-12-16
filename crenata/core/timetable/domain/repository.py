from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from crenata.core.timetable.domain.entity import Timetable


class TimetableRepository(ABC):
    @abstractmethod
    async def get_timetable(
        self,
        edu_office_code: str,
        standard_school_code: str,
        school_name: str,
        grade: int,
        room: int,
        date: datetime,
        major: Optional[str] = None,
        department: Optional[str] = None,
    ) -> Optional[list[Timetable]]:
        ...
