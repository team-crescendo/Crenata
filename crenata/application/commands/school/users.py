from discord import app_commands
from discord.interactions import Interaction

from crenata.application.client import Crenata
from crenata.application.embeds.users import school_users_embed_builder
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound
from crenata.core.user.usecases.get import GetAllSameSchoolUsersUseCase, GetUserUseCase
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="유저", description="나와 학교가 같은 유저 수를 가져옵니다.")
async def users(interaction: Interaction[Crenata]) -> None:
    user_repository = UserRepositoryImpl(interaction.client.database)
    get_user_usecase = GetUserUseCase(user_repository)

    user = await get_user_usecase.execute(interaction.user.id)

    if not user.school_info:
        raise SchoolInfoNotFound

    get_all_same_school_users_usecase = GetAllSameSchoolUsersUseCase(user_repository)

    users = await get_all_same_school_users_usecase.execute(user.school_info)

    embed = school_users_embed_builder(
        user.school_info.name, len(users), user.preferences.private
    )

    await interaction.response.send_message(
        embed=embed, ephemeral=user.preferences.ephemeral
    )
