from __future__ import annotations

from discord import Interaction
from discord.app_commands.errors import AppCommandError
from discord.app_commands.tree import CommandTree

from crenata.application.client import Crenata
from crenata.application.error.handler import ErrorHandler


class CrenataCommandTree(CommandTree[Crenata]):
    def __init__(self, client: Crenata, *, fallback_to_global: bool = True):
        super().__init__(client, fallback_to_global=fallback_to_global)
        self.error_handler: ErrorHandler[Crenata] = ErrorHandler()

    def set_error_handler(self, handler: ErrorHandler[Crenata]) -> None:
        self.error_handler = handler

    async def on_error(
        self, interaction: Interaction[Crenata], error: AppCommandError
    ) -> None:
        await self.error_handler.on_error(interaction, error)

    async def interaction_check(self, interaction: Interaction[Crenata]) -> bool: ...
