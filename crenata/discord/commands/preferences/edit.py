from crenata.discord import CrenataInteraction
from crenata.discord.commands.preferences import preferences
from crenata.utils.discord import InteractionLock
from discord import app_commands


@preferences.command(name="변경", description="환경설정을 변경합니다.")
@app_commands.describe(private="학교이름을 비공개로 할지 여부입니다.")
@app_commands.describe(ephemeral="자기 자신에게만 보이게 할지 여부입니다.")
async def preferences_edit(
    interaction: CrenataInteraction, private: bool, ephemeral: bool
) -> None:
    async with InteractionLock(interaction):
        preferences = await interaction.client.ctx.query.preferences.read(
            interaction.user.id
        )

        if not preferences:
            await interaction.response.send_message(
                content="가입되어있지 않아요.", ephemeral=True
            )
            return

        preferences.private = private
        preferences.ephemeral = ephemeral

        await interaction.client.ctx.query.preferences.update(preferences)

        await interaction.response.send_message(
            content="성공적으로 수정되었어요.",
            ephemeral=True,
        )
