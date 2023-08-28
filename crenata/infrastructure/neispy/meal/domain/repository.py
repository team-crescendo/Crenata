from neispy.client import Neispy

from crenata.core.meal.domain.entity import Meal
from crenata.core.meal.domain.repository import MealRepository
from crenata.core.school.domain.entity import School
from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.infrastructure.utils.datetime import to_datetime


class MealRepositoryImpl(MealRepository):
    def __init__(self, neispy: Neispy) -> None:
        self.neispy = neispy

    async def get_meal(self, school: School | SchoolInfo) -> list[Meal]:
        r = await self.neispy.mealServiceDietInfo(
            ATPT_OFCDC_SC_CODE=school.edu_office_code,
            SD_SCHUL_CODE=school.standard_school_code,
        )
        row = r.mealServiceDietInfo[1].row

        return [
            Meal(
                name=meal.MMEAL_SC_NM,
                dish_name=meal.DDISH_NM,
                school_name=meal.SCHUL_NM,
                calorie=meal.CAL_INFO,
                date=to_datetime(meal.MLSV_FROM_YMD),
            )
            for meal in row
        ]
