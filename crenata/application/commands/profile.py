from discord import Interaction, app_commands

from crenata.application.client import Crenata
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl
from crenata.application.embeds.profile import profile_embed_builder


@app_commands.command(name="프로필", description="내 프로필을 확인합니다.")
async def profile(interaction: Interaction[Crenata]) -> None:
    repository = UserRepositoryImpl(interaction.client.database)
    user = await GetUserUseCase(repository).execute(interaction.user.id)

    user_name = interaction.user.global_name
    if user_name == None:
        user_name = ""

    school_name = ""
    school_grade = ""
    school_room = ""

    is_private = user.preferences.private
    is_empheral = user.preferences.ephemeral

    if user.school_info != None:
        school_name = user.school_info.name
        school_grade = str(user.school_info.grade)
        school_room = str(user.school_info.room)

    embed = profile_embed_builder(
        user_name, school_name, school_grade, school_room, is_private, is_empheral
    )

    await interaction.response.send_message(embed=embed, ephemeral=is_empheral)
