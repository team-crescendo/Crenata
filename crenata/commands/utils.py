from typing import Any, Callable, Coroutine

from crenata.abc.command import AbstractCrenataCommand
from crenata.typing import P, T


def defer(
    f: Callable[..., Coroutine[Any, Any, T]]
) -> Callable[..., Coroutine[Any, Any, T]]:
    async def decorator(
        self: AbstractCrenataCommand, *args: P.args, **kwargs: P.kwargs
    ) -> T:
        await self.interaction.response.defer()
        return await f(self, *args, **kwargs)

    return decorator
