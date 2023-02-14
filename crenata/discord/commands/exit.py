from crenata.discord import CrenataInteraction
from crenata.discord.confirm import Confirm
from crenata.utils.discord import InteractionLock
from discord import Embed, app_commands


@app_commands.command(name="탈퇴", description="탈퇴합니다.")
async def exit(interaction: CrenataInteraction) -> None:
    async with InteractionLock(interaction):
        user = await interaction.client.ctx.query.user.read(interaction.user.id)

        if not user:
            await interaction.response.send_message(
                content="가입되어있지 않아요.", ephemeral=True
            )
            return

        embed = Embed(
            title="탈퇴",
            description="정말 탈퇴하시겠어요?",
            color=5681003,
        )

        view = Confirm(interaction.user.id)

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

        if not await view.wait():
            if view.agree:
                await interaction.client.ctx.query.user.delete(user)
                # edit
                await interaction.edit_original_response(
                    content="탈퇴되었습니다", embed=None, view=None
                )
                return

        await interaction.edit_original_response(
            content="취소되었습니다.", embed=None, view=None
        )
