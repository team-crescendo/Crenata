from discord import app_commands

from crenata.domain.user import User
from crenata.embed import school_result_embed_maker
from crenata.paginator import Paginator
from crenata.typing import CrenataInteraction


@app_commands.command(
    name="등록", description="학교를 등록합니다."
)  # pyright: ignore [reportGeneralTypeIssues]
@app_commands.describe(school_name="등록할 학교 이름입니다.")
async def register(interaction: CrenataInteraction, school_name: str) -> None:
    results = await interaction.client.crenata_neispy.search_school(school_name)
    view = Paginator(interaction.user.id, results, school_result_embed_maker)

    await interaction.response.send_message(embed=view.embeds[0], view=view)

    if not await view.wait():
        if view.selected:
            data = view.data[view.index]
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
            return None
        return None

    await interaction.response.edit_message(content="시간이 초과되었어요.", view=None)
