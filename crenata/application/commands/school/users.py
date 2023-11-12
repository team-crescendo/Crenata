from discord import app_commands
from discord.interactions import Interaction

from crenata.application.client import Crenata
from crenata.application.embeds.users import school_users_embed_builder
from crenata.core.user.usecases.get import GetAllSameSchoolUsersUseCase, GetUserUseCase
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="유저", description="나와 학교가 같은 유저 수를 가져옵니다.")
async def users(interaction: Interaction[Crenata]) -> None:
    user_repository = UserRepositoryImpl(interaction.client.database)
    user = await GetUserUseCase(user_repository).execute(interaction.user.id)

    assert user.school_info is not None

    users = await GetAllSameSchoolUsersUseCase(user_repository).execute(
        user.school_info
    )

    embed = school_users_embed_builder(
        user.school_info.name, len(users), user.preferences.private
    )

    await interaction.response.send_message(
        embed=embed, ephemeral=user.preferences.ephemeral
    )
