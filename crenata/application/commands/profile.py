from discord import Interaction, app_commands

from crenata.application.client import Crenata
from crenata.application.embeds.profile import profile_embed_builder
from crenata.core.schoolinfo.usecases.get import GetSchoolInfoUseCase
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.sqlalchemy.schoolinfo.domain.repository import (
    SchoolInfoRepositoryImpl,
)
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="프로필", description="내 프로필을 확인합니다.")
async def profile(interaction: Interaction[Crenata]) -> None:
    user_repository = UserRepositoryImpl(interaction.client.database)
    schoolinfo_repository = SchoolInfoRepositoryImpl(interaction.client.database)

    user = await GetUserUseCase(user_repository).execute(interaction.user.id)
    school_info = await GetSchoolInfoUseCase(schoolinfo_repository).execute(
        interaction.user.id
    )

    is_private = user.preferences.private
    is_empheral = user.preferences.ephemeral

    school_name = school_info.name
    school_grade = str(school_info.grade)
    school_room = str(school_info.room)

    embed = profile_embed_builder(
        interaction.user,
        school_name,
        school_grade,
        school_room,
        is_private,
        is_empheral,
    )

    await interaction.response.send_message(embed=embed, ephemeral=is_empheral)
