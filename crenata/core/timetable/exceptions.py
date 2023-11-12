from crenata.core.exceptions import CrenataException
from crenata.core.strings import Strings


class TimetableNotFound(CrenataException):
    def __init__(self, message: str = Strings.TIMETABLE_NOT_FOUND) -> None:
        super().__init__(message)
