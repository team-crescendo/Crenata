from datetime import datetime
from types import TracebackType

from discord.app_commands import Transformer

from crenata.application.error.exceptions import DateParseError, InteractionLocked
from crenata.infrastructure.utils.datetime import to_datetime, to_relative_date
from discord import Interaction


class ToDatetime(Transformer):
    async def transform(self, interaction: Interaction, date: str) -> datetime:
        try:
            return to_relative_date(date) or to_datetime(date)
        except ValueError:
            raise DateParseError


class InteractionLock:
    """
    인터랙션을 잠그는 클래스입니다.

    인터랙션을 잠그면 해당 유저가 다른 인터랙션을 사용할 수 없습니다.
    """

    __locked: set[int] = set()

    def __init__(self, interaction: Interaction) -> None:
        self.interaction = interaction

    async def acquire(self) -> None:
        if self.interaction.user.id in self.__locked:
            raise InteractionLocked
        self.__locked.add(self.interaction.user.id)

    async def release(self) -> None:
        self.__locked.remove(self.interaction.user.id)

    async def __aenter__(self) -> None:
        await self.acquire()

    async def __aexit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.release()


def follow_private_preference(is_private: bool, **kwargs: str) -> dict[str, str]:
    if is_private:
        kwargs = {key: "비공개" for key, _ in kwargs.items()}
    return kwargs