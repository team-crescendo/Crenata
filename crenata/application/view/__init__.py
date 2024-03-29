from __future__ import annotations

from typing import Optional

from discord import Interaction
from discord.interactions import Interaction
from discord.ui.item import Item
from discord.ui.view import View

from crenata.application.error.exceptions import NotInteractedUser, ViewTimeout
from crenata.application.error.handler import ErrorHandler


class CrenataView(View):
    def __init__(
        self,
        executor_id: int,
        timeout: Optional[float] = 60,
    ):
        super().__init__(timeout=timeout)

        self.executor_id = executor_id
        self.error_handler = ErrorHandler()

    def set_error_handler(self, handler: ErrorHandler) -> None:
        self.error_handler = handler

    async def interaction_check(self, interaction: Interaction) -> bool:
        if user := interaction.user:
            if user.id == self.executor_id:
                return True

            raise NotInteractedUser

        return False

    async def on_error(
        self, interaction: Interaction, error: Exception, _: Item[CrenataView]
    ) -> None:
        return await self.error_handler.on_error(interaction, error)

    async def on_timeout(self) -> None:
        raise ViewTimeout
