from crenata.discord import CrenataInteraction
from crenata.discord.commands.school import school
from crenata.discord.embed.school import DetailSchoolResultEmbedBuilder
from crenata.discord.interaction import school_page
from discord import app_commands


@school.command(name="검색", description="학교를 검색합니다.")
@app_commands.describe(school_name="학교 이름")
async def search(interaction: CrenataInteraction, school_name: str) -> None:
    data = await school_page(interaction, school_name)
    await interaction.edit_original_response(
        view=None, embed=DetailSchoolResultEmbedBuilder.quick_build(data)
    )
