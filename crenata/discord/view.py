from typing import Optional

from discord import Interaction
from discord.ui.view import View


class CrenataView(View):
    def __init__(
        self,
        executor_id: int,
        timeout: Optional[float] = 60,
    ):
        super().__init__(timeout=timeout)
        self.executor_id = executor_id

    async def interaction_check(self, interaction: Interaction) -> bool:
        if user := interaction.user:
            if user.id == self.executor_id:
                return True

            await interaction.response.send_message(
                "명령어 실행자만 상호작용이 가능합니다.", ephemeral=True
            )

        return False
