from discord import app_commands

from crenata.domain.user import User
from crenata.interaction import school_page
from crenata.typing import CrenataInteraction


@app_commands.command(
    name="등록", description="학교를 등록합니다."
)  # pyright: ignore [reportGeneralTypeIssues]
@app_commands.describe(school_name="등록할 학교 이름입니다.")
async def register(interaction: CrenataInteraction, school_name: str) -> None:
    await interaction.response.defer()
    data = await school_page(interaction, school_name)
    await interaction.client.orm.create_user(
        User(
            id=interaction.user.id,
            school_name=data.SCHUL_NM,
            ATPT_OFCDC_SC_CODE=data.ATPT_OFCDC_SC_CODE,
            SD_SCHUL_CODE=data.SD_SCHUL_CODE,
        )
    )
    await interaction.edit_original_response(
        content="성공적으로 등록되었어요.", embed=None, view=None
    )
