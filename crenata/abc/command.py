from abc import ABC, abstractmethod
from typing import Any, Optional

from crenata.discord import CrenataInteraction
from discord import Embed, ui
from discord.errors import NotFound
from discord.utils import MISSING


class AbstractCrenataCommand(ABC):
    def __init__(self, interaction: CrenataInteraction) -> None:
        self.interaction = interaction

    async def respond(
        self,
        content: Optional[str] = MISSING,
        embed: Optional[Embed] = MISSING,
        view: Optional[ui.View] = MISSING,
    ) -> Any:
        try:
            message = await self.interaction.original_response()
        except NotFound:
            if content is None or embed is None or view is None:
                raise ValueError(
                    "It seems intended to edit the message, "
                    "but the current context is send"
                )
            return await self.interaction.followup.send(content, embed=embed, view=view)
        else:
            r = message.edit

        return r(content=content, embed=embed, view=view)

    @abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> Any:
        ...
