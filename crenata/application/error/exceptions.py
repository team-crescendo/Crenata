from crenata.application.strings import ApplicationStrings
from crenata.core.exceptions import CrenataException


class UserCancelled(CrenataException):
    def __init__(self, message: str = ApplicationStrings.USER_CANCELLED):
        super().__init__(message)


class ViewTimeout(CrenataException):
    def __init__(self, message: str = ApplicationStrings.VIEW_TIMEOUT):
        super().__init__(message)


class DateParseError(CrenataException):
    def __init__(self, message: str = ApplicationStrings.DATE_PARSE_ERROR):
        super().__init__(message)


class MustBeGreaterThanZero(CrenataException):
    def __init__(
        self, message: str = ApplicationStrings.MUST_BE_GREATER_THAN_ZERO
    ) -> None:
        super().__init__(message)


class InteractionLocked(CrenataException):
    def __init__(self, message: str = ApplicationStrings.INTERACTION_LOCKED):
        super().__init__(message)


class NotInteractedUser(CrenataException):
    def __init__(self, message: str = ApplicationStrings.NOT_INTERACTED_USER):
        super().__init__(message)


class NeedGradeAndRoomArgument(CrenataException):
    def __init__(self, message: str = ApplicationStrings.NEED_GRADE_AND_ROOM_ARGUMENT):
        super().__init__(message)
