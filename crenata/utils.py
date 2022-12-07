from datetime import datetime
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

from discord import Interaction, app_commands
from neispy.utils import now

from crenata.abc.command import AbstractCrenataCommand
from crenata.typing import CrenataInteraction

T = TypeVar("T")
P = ParamSpec("P")


def use_crenata_command(
    cls: type[AbstractCrenataCommand],
) -> Callable[
    [Callable[..., Coroutine[Any, Any, T]]], Callable[..., Coroutine[Any, Any, T]]
]:
    def inner(
        f: Callable[..., Coroutine[Any, Any, T]]
    ) -> Callable[..., Coroutine[Any, Any, T]]:
        async def decorator(
            interaction: CrenataInteraction, *args: Any, **kwargs: Any
        ) -> T:
            for overload_command_cls in interaction.client.overload_command:
                if issubclass(cls, overload_command_cls):
                    command = overload_command_cls(interaction)
                    break
            else:
                command = cls(interaction)

            interaction.execute = command.execute

            return await f(interaction, *args, **kwargs)

        return decorator

    return inner


def defer(
    f: Callable[..., Coroutine[Any, Any, T]]
) -> Callable[..., Coroutine[Any, Any, T]]:
    async def decorator(
        interaction: CrenataInteraction, *args: Any, **kwargs: Any
    ) -> T:
        await interaction.response.defer()
        return await f(interaction, *args, **kwargs)

    return decorator


def use_current_date(
    f: Callable[P, Coroutine[Any, Any, T]]
) -> Callable[P, Coroutine[Any, Any, T]]:
    async def decorator(*args: P.args, **kwargs: P.kwargs) -> T:
        if not kwargs.get("date"):
            kwargs.update({"date": now()})
        return await f(*args, **kwargs)

    return decorator


def to_datetime(date: str) -> datetime:
    return datetime.strptime(date, "%Y%m%d")


def to_yyyymmdd(datetime: datetime) -> str:
    return datetime.strftime("%Y%m%d")


class ToDatetime(app_commands.Transformer):
    async def transform(self, interaction: Interaction, date: str) -> datetime:
        return to_datetime(date)
