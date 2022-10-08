class CrenataException(Exception):
    ...


class UserCanceled(CrenataException):
    ...


class ViewTimeout(CrenataException):
    ...
