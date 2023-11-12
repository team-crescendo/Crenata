from crenata.core.exceptions import CrenataException
from crenata.core.strings import Strings


class MajorInfoNotFound(CrenataException):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)
