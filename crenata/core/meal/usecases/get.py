from datetime import datetime
from typing import Literal, Optional

from crenata.core.meal.domain.entity import Meal
from crenata.core.meal.domain.repository import MealRepository
from crenata.core.meal.exceptions import MealNameNotFound, MealNotFound


class GetMealUseCase:
    def __init__(self, meal_repository: MealRepository) -> None:
        self.meal_repository = meal_repository

    async def execute(
        self,
        edu_office_code: str,
        standard_school_code: str,
        date: datetime,
        meal_name: Optional[Literal["조식", "중식", "석식"]] = None,
    ) -> list[Meal]:
        meals = await self.meal_repository.get_meal(
            edu_office_code, standard_school_code, date
        )

        if not meals:
            raise MealNotFound

        if meal_name:
            for meal in meals:
                if meal.name == meal_name:
                    return [meal]
            else:
                raise MealNameNotFound

        return meals
