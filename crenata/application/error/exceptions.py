from crenata.core.exceptions import CrenataException
from crenata.core.strings import Strings


class UserCancelled(CrenataException):
    def __init__(self, message: str = Strings.USER_CANCELLED):
        super().__init__(message)


class ViewTimeout(CrenataException):
    def __init__(self, message: str = Strings.VIEW_TIMEOUT):
        super().__init__(message)


class NeedSchoolRegister(CrenataException):
    def __init__(self, message: str = Strings.NEED_SCHOOL_REGISTER):
        super().__init__(message)


class DateParseError(CrenataException):
    def __init__(self, message: str = Strings.DATE_PARSE_ERROR):
        super().__init__(message)


class MustBeGreaterThanZero(CrenataException):
    def __init__(self, message: str = Strings.MEAL_NAME_NOT_FOUND) -> None:
        super().__init__(message)


class InteractionLocked(CrenataException):
    def __init__(self, message: str = Strings.INTERACTION_LOCKED):
        super().__init__(message)
