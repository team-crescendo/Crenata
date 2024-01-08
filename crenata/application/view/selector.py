from discord import ButtonStyle, Interaction
from discord.ui import Button, button

from crenata.application.view import CrenataView


class Selector(CrenataView):
    @button(label="확인", style=ButtonStyle.success, emoji="✅")
    async def confirm(self, interaction: Interaction, _: Button[CrenataView]) -> None:
        self.is_confirm = True
        await interaction.response.defer()
        self.stop()

    @button(label="닫기", style=ButtonStyle.danger, emoji="✖️")
    async def close(self, interaction: Interaction, _: Button[CrenataView]) -> None:
        self.is_confirm = False
        await interaction.response.defer()
        self.stop()
