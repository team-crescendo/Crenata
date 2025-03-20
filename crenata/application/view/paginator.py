from collections.abc import Sequence
from functools import cached_property
from typing import Optional

from discord import ButtonStyle, Interaction
from discord.ui import Button, Select, button

from crenata.application.embeds import CrenataEmbed
from crenata.application.view import CrenataView
from crenata.application.view.selector import Selector


class Paginator(CrenataView):
    """
    페이지를 넘길 수 있는 상호작용입니다.
    """

    def __init__(
        self,
        executor_id: int,
        timeout: Optional[float] = 60,
        *,
        embeds: list[CrenataEmbed] = [],
        components: Sequence[Select[CrenataView]] = [],
    ):
        super().__init__(executor_id, timeout)

        self.embeds = [
            embed.apply_page(i, len(embeds)) for i, embed in enumerate(embeds, 1)
        ]
        self.components = components
        self.index = 0

    @cached_property
    def total(self) -> int:
        return len(self.embeds)

    @button(label="이전", style=ButtonStyle.primary, emoji="◀")
    async def prev(self, interaction: Interaction, _: Button[CrenataView]) -> None:
        self.index -= 1

        if self.index < 0:
            self.index = self.total - 1

        if self.components:
            if self.index + 1 < self.total:
                self.remove_item(self.components[self.index + 1])
            else:
                self.remove_item(self.components[0])
            item = self.components[self.index]
            self.add_item(item)

        await interaction.response.edit_message(
            embed=self.embeds[self.index], view=self
        )

    @button(label="다음", style=ButtonStyle.primary, emoji="▶️")
    async def next(self, interaction: Interaction, _: Button[CrenataView]) -> None:
        self.index += 1

        if self.index >= self.total:
            self.index = 0

        if self.components:
            self.remove_item(self.components[self.index - 1])
            item = self.components[self.index]
            self.add_item(item)

        await interaction.response.edit_message(
            embed=self.embeds[self.index], view=self
        )


class SelectablePaginator(Paginator, Selector): ...
