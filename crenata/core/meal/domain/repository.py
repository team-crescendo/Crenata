from abc import ABC

from crenata.core.meal.domain.entity import Meal
from crenata.core.school.domain.entity import School
from crenata.core.schoolinfo.domain.entity import SchoolInfo


class MealRepository(ABC):
    async def get_meal(self, school: School | SchoolInfo) -> list[Meal]:
        ...
