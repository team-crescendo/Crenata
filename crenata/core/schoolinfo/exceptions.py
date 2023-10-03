from crenata.core.exceptions import CrenataException


class DuplicateSchoolInfo(CrenataException):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)


class SchoolInfoNotFound(CrenataException):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)
