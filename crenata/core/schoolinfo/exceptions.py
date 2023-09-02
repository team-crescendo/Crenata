from crenata.core.exceptions import CrenataException


class SchoolInfoNotFound(CrenataException):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)
