import asyncio
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
        major: str | None = None,
        department: str | None = None,
    ) -> list[Timetable]:
        nullable_timetable = await self.timetable_repository.get_timetable(
            edu_office_code,
            standard_school_code,
            school_name,
            grade,
            room,
            date,
            major,
            department,
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
        dates: list[datetime],
        major: str | None = None,
        department: str | None = None,
    ) -> list[list[Timetable]]:
        nullable_timetable = await asyncio.gather(
            *[
                self.timetable_repository.get_timetable(
                    edu_office_code,
                    standard_school_code,
                    school_name,
                    grade,
                    room,
                    date=date,
                    major=major,
                    department=department,
                )
                for date in dates
            ]
        )

        if all(time_table is None for time_table in nullable_timetable):
            raise TimetableNotFound

        return nullable_timetable
