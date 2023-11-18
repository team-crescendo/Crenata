import asyncio
from datetime import datetime, timedelta
from functools import partial

from neispy.client import Neispy
from neispy.error import DataNotFound

from crenata.core.timetable.domain.entity import Timetable
from crenata.core.timetable.domain.repository import TimetableRepository
from crenata.infrastructure.neispy.timetable.domain.entity import TimetableAdapter
from crenata.infrastructure.utils.datetime import to_yyyymmdd


class TimetableRepositoryImpl(TimetableRepository):
    def __init__(self, neispy: Neispy) -> None:
        self.neispy = neispy

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
        if school_name.endswith("초등학교"):
            func = self.neispy.elsTimetable
        elif school_name.endswith("중학교"):
            func = self.neispy.misTimetable
        elif school_name.endswith("고등학교"):
            func = self.neispy.hisTimetable
            if major and department:
                func = partial(func, **{"ORD_SC_NM": department, "DDDEP_NM": major})
        else:
            return None

        ay = date.year if date.month > 2 else date.year - 1
        sem = 1 if 2 < date.month < 8 else 2

        try:
            r = await func(
                ATPT_OFCDC_SC_CODE=edu_office_code,
                SD_SCHUL_CODE=standard_school_code,
                AY=str(ay),
                SEM=str(sem),
                ALL_TI_YMD=int(to_yyyymmdd(date)),
                GRADE=str(grade),
                CLASS_NM=str(room),
            )
        except DataNotFound:
            return None

        head = next(iter(r.__dict__.values()))[1]

        return [TimetableAdapter.from_neispy(timetable) for timetable in head.row]

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
        # get previous and next weekdays
        # only monday to friday included current date
        dates = [
            date + timedelta(days=i) for i in range(-date.weekday(), 5 - date.weekday())
        ]

        # get all time tables
        time_tables = await asyncio.gather(
            *[
                self.get_timetable(
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
        # check all results is None
        if all(time_table is None for time_table in time_tables):
            time_tables = None

        return time_tables
