from typing import Any, Optional

from crenata.discord.view import CrenataView
from discord.enums import ButtonStyle
from discord.interactions import Interaction
from discord.ui.button import button


class Selector(CrenataView):
    def __init__(
        self,
        executor_id: int,
        timeout: Optional[float] = 60,
    ):
        super().__init__(executor_id=executor_id, timeout=timeout)
        self.executor_id = executor_id

    @button(label="확인", style=ButtonStyle.success, emoji="✅")
    async def confirm(self, interaction: Interaction, _: Any) -> None:
        self.selected = True
        await interaction.response.defer()
        self.stop()

    @button(label="닫기", style=ButtonStyle.danger, emoji="✖️")
    async def close(self, interaction: Interaction, _: Any) -> None:
        await interaction.response.defer()
        self.stop()
