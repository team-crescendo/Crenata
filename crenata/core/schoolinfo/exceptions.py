from crenata.core.exceptions import CrenataException
from crenata.core.strings import CoreStrings


class DuplicateSchoolInfo(CrenataException):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)


class SchoolInfoNotFound(CrenataException):
    def __init__(self, message: str = CoreStrings.SCHOOL_INFO_NOT_FOUND) -> None:
        super().__init__(message)
