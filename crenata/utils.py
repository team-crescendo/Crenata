from datetime import datetime
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar
from discord import app_commands, Interaction

from neispy.utils import now

T = TypeVar("T")
P = ParamSpec("P")


def use_current_date(
    f: Callable[P, Coroutine[Any, Any, T]]
) -> Callable[P, Coroutine[Any, Any, T]]:
    async def decorator(*args: P.args, **kwargs: P.kwargs) -> T:
        if not kwargs.get("date"):
            kwargs.update({"date": now()})
        return await f(*args, **kwargs)

    return decorator


def to_datetime(date: str):
    return datetime.strptime(date, "%Y%m%d")


def to_yyyymmdd(datetime: datetime):
    return datetime.strftime("%Y%m%d")


class ToDatetime(app_commands.Transformer):
    async def transform(self, interaction: Interaction, date: str) -> datetime:
        return to_datetime(date)
