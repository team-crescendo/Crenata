from datetime import datetime
from typing import Any, Callable, Coroutine

from crenata.typing import P, T
from discord import Interaction, app_commands
from neispy.utils import KST


def use_current_date(
    f: Callable[P, Coroutine[Any, Any, T]]
) -> Callable[P, Coroutine[Any, Any, T]]:
    async def decorator(*args: P.args, **kwargs: P.kwargs) -> T:
        if not kwargs.get("date"):
            kwargs.update({"date": datetime.now(KST)})
        return await f(*args, **kwargs)

    return decorator


def to_datetime(date: str) -> datetime:
    return datetime.strptime(date, "%Y%m%d")


def to_yyyymmdd(datetime: datetime) -> str:
    return datetime.strftime("%Y%m%d")


class ToDatetime(app_commands.Transformer):
    async def transform(self, interaction: Interaction, date: str) -> datetime:
        return to_datetime(date)
