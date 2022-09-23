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
        /,
        date: Optional[str] = None,
    ) -> Optional[Any]:
        if results := await self.mealServiceDietInfo(
            ATPT_OFCDC_SC_CODE=edu_office_code,
            SD_SCHUL_CODE=standard_school_code,
            MLSV_YMD=date,
        ):
            for result in results:
                if result.MMEAL_SC_NM == meal_time:
                    return result

        return None
