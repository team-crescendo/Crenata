from crenata.core.exceptions import CrenataException
from crenata.core.strings import Strings


class UserNotFound(CrenataException):
    def __init__(self, message: str = Strings.USER_NOT_FOUND) -> None:
        super().__init__(message)


class DuplicateUser(CrenataException):
    def __init__(self, message: str = Strings.DUPLICATE_USER) -> None:
        super().__init__(message)
