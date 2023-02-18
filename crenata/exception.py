class CrenataException(Exception):
    def __init__(self, *, edit: bool = False):
        self.edit = edit


class UserCanceled(CrenataException):
    """취소했어요 :("""

    def __init__(self, *, edit: bool = True):
        super().__init__(edit=edit)


class ViewTimeout(CrenataException):
    """시간이 초과되었어요."""

    def __init__(self, *, edit: bool = True):
        super().__init__(edit=edit)


class NeedSchoolRegister(CrenataException):
    """학교를 등록해주세요."""


class NeedGradeAndRoom(CrenataException):
    """학년과 반을 입력해주세요."""


class NeedSchoolName(CrenataException):
    """가입되어있지 않은경우 학교명을 입력해주셔야 해요."""


class DateParseError(CrenataException):
    """날짜를 잘못 입력한것 같아요. YYYYMMDD 형식, 또는 "어제, 내일"로 입력해주세요. 예: 20220110, 내일"""


class MustBeGreaterThanOne(CrenataException):
    """학년 또는 반은 0보다 커야해요."""


class InteractionLocked(CrenataException):
    """다른 명령어을 사용중일때는 해당 명령어를 사용할수없어요."""
