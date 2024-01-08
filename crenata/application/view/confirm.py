from discord import ButtonStyle, Interaction
from discord.ui import Button, button

from crenata.application.view import CrenataView


class Confirm(CrenataView):
    """
    확인 버튼과 취소 버튼이 있는 상호작용입니다.
    """

    @button(label="확인", style=ButtonStyle.green, emoji="✅")
    async def confirm(self, interaction: Interaction, _: Button[CrenataView]) -> None:
        self.is_confirm = True

        await interaction.response.defer()
        self.stop()

    @button(label="취소", style=ButtonStyle.red, emoji="✖️")
    async def cancel(self, interaction: Interaction, _: Button[CrenataView]) -> None:
        self.is_confirm = False

        await interaction.response.defer()
        self.stop()
