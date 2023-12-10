from datetime import datetime
from typing import Optional

from neispy.client import Neispy
from neispy.error import DataNotFound

from crenata.core.meal.domain.entity import Meal
from crenata.core.meal.domain.repository import MealRepository
from crenata.infrastructure.neispy.meal.domain.entity import MealAdapter
from crenata.infrastructure.utils.datetime import to_yyyymmdd


class MealRepositoryImpl(MealRepository):
    def __init__(self, neispy: Neispy) -> None:
        self.neispy = neispy

    async def get_meal(
        self, edu_office_code: str, standard_school_code: str, date: datetime
    ) -> Optional[list[Meal]]:
        try:
            r = await self.neispy.mealServiceDietInfo(
                ATPT_OFCDC_SC_CODE=edu_office_code,
                SD_SCHUL_CODE=standard_school_code,
                MLSV_YMD=to_yyyymmdd(date),
            )

        except DataNotFound:
            return None

        row = r.mealServiceDietInfo[1].row

        return [MealAdapter.from_neispy(meal) for meal in row]
