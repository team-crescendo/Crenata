from crenata.core.exceptions import CrenataException
from crenata.core.strings import CoreStrings


class MealNotFound(CrenataException):
    def __init__(self, message: str = CoreStrings.MEAL_NOT_FOUND) -> None:
        super().__init__(message)


class MealNameNotFound(CrenataException):
    def __init__(self, message: str = CoreStrings.MEAL_NAME_NOT_FOUND) -> None:
        super().__init__(message)
