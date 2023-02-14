from __future__ import annotations

import asyncio
from datetime import datetime, timedelta
from typing import Any, Literal, Optional, cast

from aiohttp.client import ClientSession

from crenata.utils.datetime import to_yyyymmdd, use_current_date
from neispy.client import Neispy


class CrenataNeispy(Neispy):
    def __init__(
        self,
        KEY: Optional[str] = None,
        Type: Literal["json", "xml"] = "json",
        pIndex: int = 1,
        pSize: int = 100,
        session: Optional[ClientSession] = None,
        only_rows: bool = True,
    ) -> None:
        super().__init__(KEY, Type, pIndex, pSize, session, only_rows)

    @classmethod
    def create(cls, key: str) -> CrenataNeispy:
        return cls(key)

    async def search_school(self, school_name: str) -> Any:
        return await self.schoolInfo(SCHUL_NM=school_name)

    @use_current_date
    async def get_meal(
        self,
        edu_office_code: str,
        standard_school_code: str,
        meal_time: Optional[Literal["조식", "중식", "석식"]] = None,
        *,
        date: Optional[datetime],
    ) -> Optional[list[Any]]:
        """
        학교 급식 정보를 가져옵니다.
        """
        assert date
        if results := await self.mealServiceDietInfo(
            ATPT_OFCDC_SC_CODE=edu_office_code,
            SD_SCHUL_CODE=standard_school_code,
            MLSV_YMD=to_yyyymmdd(date),
        ):
            if not meal_time:
                return cast(list[Any], results)

            for result in results:
                if result.MMEAL_SC_NM == meal_time:
                    return [result]

            return None

        return cast(list[Any], results)

    @use_current_date
    async def get_time_table(
        self,
        edu_office_code: str,
        standard_school_code: str,
        school_name: str,
        grade: int,
        room: int,
        *,
        date: Optional[datetime],
    ) -> Optional[Any]:
        """
        학교 시간표 정보를 가져옵니다.
        """
        assert date

        if school_name.endswith("초등학교"):
            func = self.elsTimetable
        elif school_name.endswith("중학교"):
            func = self.misTimetable
        elif school_name.endswith("고등학교"):
            func = self.hisTimetable
        else:
            return None

        ay = date.year if date.month > 2 else date.year - 1
        sem = 1 if date.month > 2 and date.month < 8 else 2

        return await func(
            ATPT_OFCDC_SC_CODE=edu_office_code,
            SD_SCHUL_CODE=standard_school_code,
            AY=ay,
            SEM=sem,
            ALL_TI_YMD=int(to_yyyymmdd(date)),
            GRADE=grade,
            CLASS_NM=str(room),
        )

    @use_current_date
    async def get_week_time_table(
        self,
        edu_office_code: str,
        standard_school_code: str,
        school_name: str,
        grade: int,
        room: int,
        *,
        date: Optional[datetime],
    ) -> tuple[Optional[list[Any]], datetime]:
        """
        학교 주간 시간표 정보를 가져옵니다.
        """
        assert date
        # get previous and next weekdays
        # only monday to friday included current date
        dates = [
            date + timedelta(days=i) for i in range(-date.weekday(), 5 - date.weekday())
        ]

        # get all time tables
        time_tables = await asyncio.gather(
            *[
                self.get_time_table(
                    edu_office_code,
                    standard_school_code,
                    school_name,
                    grade,
                    room,
                    date=date,
                )
                for date in dates
            ]
        )

        # check all results is None
        if all(time_table is None for time_table in time_tables):
            time_tables = None

        return time_tables, date
