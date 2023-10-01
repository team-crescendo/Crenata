from crenata.core.exceptions import CrenataException
from crenata.core.strings import Strings


class MealNameNotFound(CrenataException):
    def __init__(
        self, message: str = Strings.MEAL_NAME_NOT_FOUND
    ) -> None:
        super().__init__(message)
