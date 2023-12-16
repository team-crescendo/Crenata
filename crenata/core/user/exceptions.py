from crenata.core.exceptions import CrenataException
from crenata.core.strings import CoreStrings


class UserNotFound(CrenataException):
    def __init__(self, message: str = CoreStrings.USER_NOT_FOUND) -> None:
        super().__init__(message)


class DuplicateUser(CrenataException):
    def __init__(self, message: str = CoreStrings.DUPLICATE_USER) -> None:
        super().__init__(message)
