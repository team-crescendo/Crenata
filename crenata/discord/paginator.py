from functools import cached_property
from typing import Any, Optional

from crenata.discord.selecter import Selector
from crenata.discord.view import CrenataView
from crenata.utils.discord import CrenataEmbed
from discord.enums import ButtonStyle
from discord.interactions import Interaction
from discord.ui.button import button


class Paginator(CrenataView):
    """
    페이지를 넘길수있는 상호작용입니다.
    """

    def __init__(
        self,
        executor_id: int,
        embeds: list[CrenataEmbed],
        timeout: Optional[float] = 60,
    ):
        super().__init__(timeout=timeout, executor_id=executor_id)
        self.embeds = embeds
        self.index = 0

    @cached_property
    def total(self) -> int:
        return len(self.embeds)

    @button(label="이전", style=ButtonStyle.primary, emoji="◀")
    async def prev(self, interaction: Interaction, _: Any) -> None:
        self.index -= 1

        if self.index < 0:
            self.index = self.total - 1

        await interaction.response.edit_message(embed=self.embeds[self.index])

    @button(label="다음", style=ButtonStyle.primary, emoji="▶️")
    async def next(self, interaction: Interaction, _: Any) -> None:
        self.index += 1

        if self.index >= self.total:
            self.index = 0

        await interaction.response.edit_message(embed=self.embeds[self.index])


class SelectablePaginator(Paginator, Selector):
    ...
