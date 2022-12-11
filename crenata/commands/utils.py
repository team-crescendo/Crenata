from contextlib import suppress
from typing import Any, Callable, Coroutine

from crenata.abc.command import AbstractCrenataCommand
from crenata.typing import P, T
from discord.errors import InteractionResponded


def defer(
    f: Callable[..., Coroutine[Any, Any, T]]
) -> Callable[..., Coroutine[Any, Any, T]]:
    async def decorator(
        self: AbstractCrenataCommand, *args: P.args, **kwargs: P.kwargs
    ) -> T:
        with suppress(InteractionResponded):
            await self.interaction.response.defer()

        return await f(*args, **kwargs)

    return decorator
