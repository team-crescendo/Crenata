from discord import Embed, Interaction, app_commands

from crenata.application.client import Crenata
from crenata.application.utils import InteractionLock
from crenata.application.view.confirm import Confirm
from crenata.core.strings import Strings
from crenata.core.user.usecases.delete import DeleteUserUseCase
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="탈퇴", description="탈퇴합니다.")
async def exit(interaction: Interaction[Crenata]) -> None:
    async with InteractionLock(interaction):
        user_repository = UserRepositoryImpl(interaction.client.database)

        user = await GetUserUseCase(user_repository).execute(interaction.user.id)

        embed = Embed(
            title="탈퇴",
            description="정말 탈퇴하시겠습니까?",
            color=5681003,
        )

        view = Confirm(interaction.user.id)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

        if not await view.wait():
            if view.is_confirm:
                await DeleteUserUseCase(user_repository).execute(user)
                await interaction.edit_original_response(
                    content="탈퇴 되었습니다.", embed=None, view=None
                )
                return

        await interaction.edit_original_response(
            content=Strings.USER_CANCELLED, embed=None, view=None
        )
