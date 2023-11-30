from discord import Interaction, app_commands

from crenata.application.client import Crenata
from crenata.application.embeds.exit import exit_embed_builder
from crenata.application.strings import ApplicationStrings
from crenata.application.utils import InteractionLock
from crenata.application.view.confirm import Confirm
from crenata.core.user.usecases.delete import DeleteUserUseCase
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="탈퇴", description="탈퇴합니다.")
async def exit(interaction: Interaction[Crenata]) -> None:
    async with InteractionLock(interaction):
        user_repository = UserRepositoryImpl(interaction.client.database)

        user = await GetUserUseCase(user_repository).execute(interaction.user.id)

        embed = exit_embed_builder()

        view = Confirm(interaction.user.id)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

        if not await view.wait():
            if view.is_confirm:
                await DeleteUserUseCase(user_repository).execute(user)
                await interaction.edit_original_response(
                    content=ApplicationStrings.UNREGISTER_COMPLETED,
                    embed=None,
                    view=None,
                )
                return

        await interaction.edit_original_response(
            content=ApplicationStrings.USER_CANCELLED, embed=None, view=None
        )
