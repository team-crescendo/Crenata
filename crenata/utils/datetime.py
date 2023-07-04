from datetime import datetime, timedelta
from typing import Any, Callable, Coroutine, Optional

from crenata.typing import P, T
from neispy.utils import KST


def use_current_date(
    f: Callable[P, Coroutine[Any, Any, T]]
) -> Callable[P, Coroutine[Any, Any, T]]:
    """
    날짜 인자가 없을 경우 현재 날짜를 사용하는 데코레이터입니다.
    """

    async def decorator(*args: P.args, **kwargs: P.kwargs) -> T:
        if not kwargs.get("date"):
            kwargs.update({"date": datetime.now(KST)})
        return await f(*args, **kwargs)

    return decorator


def to_datetime(date: str) -> datetime:
    """
    YYYYMMDD 형식의 문자열을 datetime으로 변환합니다.
    """
    return datetime.strptime(date.strip(), "%Y%m%d")


def to_yyyymmdd(datetime: datetime) -> str:
    """
    datetime을 YYYYMMDD 형식의 문자열로 변환합니다.
    """
    return datetime.strftime("%Y%m%d")


def datetime_to_readable(date: datetime) -> str:
    """
    datetime을 YYYY년 MM월 DD일 형식의 문자열로 변환합니다.
    """
    return date.strftime("%Y{} %m{} %d{}").format("년", "월", "일")


def to_weekday(date: datetime) -> str:
    """
    datetime을 요일로 변환합니다.
    """
    days = ["월", "화", "수", "목", "금", "토", "일"]
    day = date.weekday()
    return days[day]


def to_relative_date(keyword: str) -> Optional[datetime]:
    """
    "내일"과 같은 상대적인 날짜를 datetime으로 변환합니다.
    """
    if keyword == "내일":
        return datetime.now(KST) + timedelta(days=1)
    return None
