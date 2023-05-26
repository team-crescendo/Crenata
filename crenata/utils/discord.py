from datetime import datetime
from types import TracebackType
from typing import Any, Optional

from discord.colour import Colour
from discord.types.embed import EmbedType

from crenata.exception import DateParseError, InteractionLocked
from crenata.typing import InnerSend
from crenata.utils.datetime import to_datetime, to_relative_date
from discord import Interaction, InteractionMessage, app_commands, Embed
from discord.errors import NotFound
from discord.utils import MISSING


class CrenataEmbed(Embed):
    def __init__(
        self,
        *,
        colour: int | Colour | None = None,
        color: int | Colour | None = 5681003,
        title: Any | None = None,
        type: EmbedType = "rich",
        url: Any | None = None,
        description: Any | None = None,
        timestamp: datetime | None = None,
    ):
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp,
        )

    def apply_pagination(self, index: int, total: int) -> None:
        self.set_footer(text=f"{index}/{total}")


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


class ToDatetime(app_commands.Transformer):
    async def transform(self, interaction: Interaction, date: str) -> datetime:
        try:
            return to_relative_date(date) or to_datetime(date)
        except ValueError:
            raise DateParseError


async def get_message(interaction: Interaction) -> Optional[InteractionMessage]:
    """
    인터랙션의 원래 메시지를 가져옵니다.
    """
    try:
        message = await interaction.original_response()
    except NotFound:
        return None
    else:
        return message


def dynamic_send(
    interaction: Interaction,
) -> InnerSend:
    """
    인터렉션이 원래 메시지를 가지고 있다면 원래 메시지를 수정하고

    아니라면 새로운 메시지를 보내는 함수를 반환합니다.
    """

    async def inner_send(*, followup: bool = False, **kwargs: Any) -> None:
        msg = await get_message(interaction)

        if msg and not "file" in kwargs:
            if "ephemeral" in kwargs:
                del kwargs["ephemeral"]
            await msg.edit(**kwargs)
            return

        for k, v in kwargs.items():
            if v is None:
                kwargs[k] = MISSING

        if followup:
            await interaction.followup.send(**kwargs)
            return

        await interaction.response.send_message(**kwargs)

    return inner_send


def follow_private_preference(*, private: bool, **kwargs: Any) -> dict[str, str]:
    if private:
        kwargs = {key: "비공개" for key, _ in kwargs.items()}
    return kwargs
