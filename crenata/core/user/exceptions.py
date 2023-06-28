from crenata.core.exceptions import CrenataException


class UserNotFound(CrenataException):
    ...


class DuplicateUser(CrenataException):
    ...
