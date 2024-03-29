from crenata.core.exceptions import CrenataException
from crenata.core.strings import CoreStrings


class TimetableNotFound(CrenataException):
    def __init__(self, message: str = CoreStrings.TIMETABLE_NOT_FOUND) -> None:
        super().__init__(message)
