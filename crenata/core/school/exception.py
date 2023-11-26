from crenata.core.exceptions import CrenataException
from crenata.core.strings import CoreStrings


class SchoolNotFound(CrenataException):
    def __init__(self, message: str = CoreStrings.SCHOOL_NOT_FOUND) -> None:
        super().__init__(message)
