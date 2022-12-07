from functools import cached_property
from typing import Any, Optional

from crenata.typing import EmbedMaker
from discord.embeds import Embed
from discord.enums import ButtonStyle
from discord.interactions import Interaction
from discord.ui.button import button
from discord.ui.view import View


class Paginator(View):
    def __init__(
        self,
        executor_id: int,
        data: list[Any],
        embed_maker: EmbedMaker,
        timeout: Optional[float] = 60,
    ):
        super().__init__(timeout=timeout)
        self.data = data
        self.embed_maker: EmbedMaker = embed_maker
        self.executor_id = executor_id
        self.index = 0
        self.selected = False

    @cached_property
    def total(self) -> int:
        return len(self.data)

    @cached_property
    def embeds(self) -> list[Embed]:
        return [self.embed_maker(d, i, self.total) for i, d in enumerate(self.data, 1)]

    async def interaction_check(self, interaction: Interaction) -> bool:
        if user := interaction.user:
            if user.id == self.executor_id:
                return True

            await interaction.response.send_message(
                "명령어 실행자만 상호작용이 가능합니다.", ephemeral=True
            )

        return False

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

    @button(label="확인", style=ButtonStyle.success, emoji="✅")
    async def ok(self, interaction: Interaction, _: Any) -> None:
        self.selected = True
        await interaction.response.defer()
        self.stop()

    @button(label="닫기", style=ButtonStyle.danger, emoji="❌")
    async def close(self, interaction: Interaction, _: Any) -> None:
        await interaction.response.defer()
        self.stop()
