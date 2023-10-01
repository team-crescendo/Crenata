from typing import Any, Optional

from discord.interactions import Interaction
from discord.ui.item import Item
from discord.ui.view import View

from crenata.application.error.exceptions import ViewTimeout
from crenata.application.error.handler import ErrorHandler
from discord import Interaction


class CrenataView(View):
    def __init__(
        self,
        executor_id: int,
        timeout: Optional[float] = 60,
    ):
        super().__init__(timeout=timeout)
        self.executor_id = executor_id
        self.error_handler: ErrorHandler[Any] = ErrorHandler()

    def set_error_handler(self, handler: ErrorHandler[Any]) -> None:
        self.error_handler = handler

    async def interaction_check(self, interaction: Interaction) -> bool:
        if user := interaction.user:
            if user.id == self.executor_id:
                return True

            # TODO: Raise

        return False

    async def on_error(
        self, interaction: Interaction, error: Exception, item: Item[Any]
    ) -> None:
        original = error.__cause__
        assert original is not None
        callback = self.error_handler.lookup(original)
        if callback:
            return await callback(interaction, original)

        raise error

    async def on_timeout(self) -> None:
        raise ViewTimeout
