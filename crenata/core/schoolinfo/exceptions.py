from crenata.core.exceptions import CrenataException
from crenata.core.strings import Strings


class DuplicateSchoolInfo(CrenataException):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)


class SchoolInfoNotFound(CrenataException):
    def __init__(self, message: str = Strings.SCHOOL_INFO_NOT_FOUND) -> None:
        super().__init__(message)
