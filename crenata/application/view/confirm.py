from typing import Any

from crenata.application.view import CrenataView
from discord import ButtonStyle, Interaction, ui


class Confirm(CrenataView):
    """
    확인 버튼과 취소 버튼이 있는 상호작용입니다.
    """

    @ui.button(label="확인", style=ButtonStyle.green, emoji="✅")
    async def confirm(self, interaction: Interaction, _: ui.Button[Any]) -> None:
        self.is_confirm = True
        await interaction.response.defer()
        self.stop()

    @ui.button(label="취소", style=ButtonStyle.red, emoji="✖️")
    async def cancel(self, interaction: Interaction, button: ui.Button[Any]) -> None:
        self.is_confirm = False
        await interaction.response.defer()
        self.stop()
