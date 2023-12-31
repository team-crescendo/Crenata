import asyncio
from datetime import datetime
from typing import Optional, cast

from crenata.core.timetable.domain.entity import Timetable
from crenata.core.timetable.domain.repository import TimetableRepository
from crenata.core.timetable.exceptions import TimetableNotFound


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
        major: Optional[str] = None,
        department: Optional[str] = None,
    ) -> list[list[Timetable]]:
        nullable_timetable = await asyncio.gather(
            *[
                self.timetable_repository.get_timetable(
                    edu_office_code,
                    standard_school_code,
                    school_name,
                    grade,
                    room,
                    date,
                    major,
                    department,
                )
                for date in dates
            ]
        )

        if not all(timetable for timetable in nullable_timetable):
            raise TimetableNotFound

        return cast(list[list[Timetable]], nullable_timetable)
