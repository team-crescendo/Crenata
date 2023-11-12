from datetime import datetime

from crenata.core.timetable.domain.entity import Timetable
from crenata.core.timetable.domain.repository import TimetableRepository
from crenata.core.timetable.exceptions import TimetableNotFound


class GetTimetableUseCase:
    def __init__(self, timetable_repository: TimetableRepository) -> None:
        self.timetable_repository = timetable_repository

    async def execute(
        self,
        edu_office_code: str,
        standard_school_code: str,
        school_name: str,
        grade: int,
        room: int,
        date: datetime,
    ) -> list[Timetable]:
        nullable_timetable = await self.timetable_repository.get_timetable(
            edu_office_code, standard_school_code, school_name, grade, room, date
        )

        if nullable_timetable is None:
            raise TimetableNotFound

        return nullable_timetable


class GetWeekTimetableUseCase:
    def __init__(self, timetable_repository: TimetableRepository) -> None:
        self.timetable_repository = timetable_repository

    async def execute(
        self,
        edu_office_code: str,
        standard_school_code: str,
        school_name: str,
        grade: int,
        room: int,
        date: datetime,
    ) -> list[list[Timetable]]:
        nullable_timetable = await self.timetable_repository.get_week_timetable(
            edu_office_code, standard_school_code, school_name, grade, room, date
        )

        if nullable_timetable is None:
            raise TimetableNotFound

        return nullable_timetable
