from __future__ import annotations

from typing import Any, Literal, Optional

from aiohttp.client import ClientSession
from neispy.client import Neispy

from crenata.utils import use_current_date


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
        if results := await self.schoolInfo(SCHUL_NM=school_name):
            return results

    @use_current_date
    async def get_meal(
        self,
        meal_time: Literal["조식", "중식", "석식"],
        edu_office_code: str,
        standard_school_code: str,
        *,
        date: Optional[str],
    ) -> Optional[Any]:
        """
        학교 급식 정보를 가져옵니다.
        """
        if results := await self.mealServiceDietInfo(
            ATPT_OFCDC_SC_CODE=edu_office_code,
            SD_SCHUL_CODE=standard_school_code,
            MLSV_YMD=date,
        ):
            for result in results:
                if result.MMEAL_SC_NM == meal_time:
                    return result

        return None

    @use_current_date
    async def get_time_table(
        self,
        edu_office_code: str,
        standard_school_code: str,
        school_name: str,
        grade: int,
        class_num: int,
        *,
        date: Optional[str],
    ) -> Optional[Any]:
        """
        학교 시간표 정보를 가져옵니다.
        """
        assert date
        func = None

        if school_name.endswith("초등학교"):
            func = self.elsTimetable
        elif school_name.endswith("중학교"):
            func = self.misTimetable
        elif school_name.endswith("고등학교"):
            func = self.hisTimetable
        else:
            return None

        year = int(date[0:4])
        month = int(date[4:6])

        ay = year if month > 2 else year - 1
        sem = 1 if month > 2 and month < 8 else 2

        print(year, month, ay, sem, grade, class_num)

        return await func(
            ATPT_OFCDC_SC_CODE=edu_office_code,
            SD_SCHUL_CODE=standard_school_code,
            AY=ay,
            SEM=sem,
            ALL_TI_YMD=int(date),
            GRADE=grade,
            CLASS_NM=str(class_num),
        )
