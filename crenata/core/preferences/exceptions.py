from crenata.core.exceptions import CrenataException
from crenata.core.strings import CoreStrings


class PreferencesNotFound(CrenataException):
    def __init__(self, message: str = CoreStrings.PREFERENCES_NOT_FOUND) -> None:
        super().__init__(message)
