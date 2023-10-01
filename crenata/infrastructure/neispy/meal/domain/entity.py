from dataclasses import dataclass

from neispy.domain.mealservicedietinfo import MealServiceDietInfoRow

from crenata.core.meal.domain.entity import Meal
from crenata.infrastructure.utils.datetime import to_datetime


@dataclass
class MealAdapter(Meal):
    @classmethod
    def from_neispy(cls, meal: MealServiceDietInfoRow) -> Meal:
        return cls(
            name=meal.MMEAL_SC_NM,
            dish_name=meal.DDISH_NM,
            school_name=meal.SCHUL_NM,
            calorie=meal.CAL_INFO,
            date=to_datetime(meal.MLSV_FROM_YMD),
        )
