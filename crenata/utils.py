from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

from neispy.utils import now

T = TypeVar("T")
P = ParamSpec("P")


def use_current_date(
    f: Callable[P, Coroutine[Any, Any, T]]
) -> Callable[P, Coroutine[Any, Any, T]]:
    async def decorator(*args: P.args, **kwargs: P.kwargs) -> T:
        if not kwargs["date"]:
            kwargs.update({"date": now()})
        return await f(*args, **kwargs)

    return decorator
