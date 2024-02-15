from __future__ import annotations

from discord import Interaction
from discord._types import ClientT
from discord.app_commands.errors import AppCommandError
from discord.app_commands.tree import CommandTree

from crenata.application.error.handler import ErrorHandler


class CrenataCommandTree(CommandTree[ClientT]):
    def __init__(self, client: ClientT, *, fallback_to_global: bool = True):
        super().__init__(client, fallback_to_global=fallback_to_global)
        self.error_handler: ErrorHandler[ClientT] = ErrorHandler()

    def set_error_handler(self, handler: ErrorHandler[ClientT]) -> None:
        self.error_handler = handler

    async def on_error(
        self, interaction: Interaction[ClientT], error: AppCommandError
    ) -> None:
        await self.error_handler.on_error(interaction, error)

    async def interaction_check(self, interaction: Interaction[ClientT]) -> bool:
        ...
