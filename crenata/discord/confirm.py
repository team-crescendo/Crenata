from typing import Any

from discord import ButtonStyle, Interaction, ui


class Confirm(ui.View):
    """
    확인 버튼과 취소 버튼이 있는 상호작용입니다.
    """

    def __init__(self, executor_id: int) -> None:
        super().__init__(timeout=60.0)
        self.agree: bool = False
        self.executor_id: int = executor_id

    async def interaction_check(self, interaction: Interaction) -> bool:
        if user := interaction.user:
            if user.id == self.executor_id:
                return True

            await interaction.response.send_message(
                "명령어 실행자만 상호작용이 가능합니다.", ephemeral=True
            )

        return False

    @ui.button(label="확인", style=ButtonStyle.green, emoji="✅")
    async def confirm(self, interaction: Interaction, _: ui.Button[Any]) -> None:
        self.agree = True
        await interaction.response.defer()
        self.stop()

    @ui.button(label="취소", style=ButtonStyle.red, emoji="✖️")
    async def cancel(self, interaction: Interaction, button: ui.Button[Any]) -> None:
        await interaction.response.defer()
        self.stop()
