from abc import ABC, abstractmethod
from datetime import datetime

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
        major: str | None = None,
        department: str | None = None,
    ) -> list[Timetable] | None:
        ...

    @abstractmethod
    async def get_week_timetable(
        self,
        edu_office_code: str,
        standard_school_code: str,
        school_name: str,
        grade: int,
        room: int,
        date: datetime,
        major: str | None = None,
        department: str | None = None,
    ) -> list[list[Timetable]] | None:
        ...
