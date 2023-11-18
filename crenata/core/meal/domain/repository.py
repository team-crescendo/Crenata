from abc import ABC, abstractmethod
from datetime import datetime

from crenata.core.meal.domain.entity import Meal


class MealRepository(ABC):
    @abstractmethod
    async def get_meal(
        self, edu_office_code: str, standard_school_code: str, date: datetime
    ) -> list[Meal] | None:
        ...
