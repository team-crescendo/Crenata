from discord import Interaction, app_commands

from crenata.application.client import Crenata
from crenata.application.embeds.profile import profile_embed_builder
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="프로필", description="내 프로필을 확인합니다.")
async def profile(interaction: Interaction[Crenata]) -> None:
    user_repository = UserRepositoryImpl(interaction.client.database)
    get_user_usecase = GetUserUseCase(user_repository)

    user = await get_user_usecase.execute(interaction.user.id)

    is_private = user.preferences.private
    is_empheral = user.preferences.ephemeral

    embed = profile_embed_builder(
        interaction.user,
        user.school_info,
        is_private,
        is_empheral,
    )

    await interaction.response.send_message(embed=embed, ephemeral=is_empheral)
