from discord import app_commands
from discord.interactions import Interaction

from crenata.application.client import Crenata
from crenata.application.embeds.school import detail_school_school_embed_builder
from crenata.application.interaction import school_page
from crenata.core.school.usecases.get import GetSchoolUseCase
from crenata.infrastructure.neispy.school.domain.repository import SchoolRepositoryImpl


@app_commands.command(name="검색", description="학교를 검색합니다.")
@app_commands.describe(school_name="학교 이름")
async def search(interaction: Interaction[Crenata], school_name: str) -> None:
    school_repository = SchoolRepositoryImpl(interaction.client.neispy)
    get_school_usecase = GetSchoolUseCase(school_repository)

    school_infos = await get_school_usecase.execute(school_name)

    school_info = await school_page(interaction, school_infos)

    embed = detail_school_school_embed_builder(school_info)

    await interaction.edit_original_response(view=None, embed=embed)
