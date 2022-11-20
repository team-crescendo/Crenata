from datetime import datetime
from typing import Literal, Optional

from discord import app_commands

from crenata.interaction import school_page
from crenata.typing import CrenataInteraction
from crenata.utils import ToDatetime


@app_commands.command(
    name="급식", description="급식 식단표를 가져와요."
)  # pyright: ignore [reportGeneralTypeIssues]
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(meal_time="시간")
@app_commands.describe(date="날짜")
async def meal(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    meal_time: Optional[Literal["조식", "중식", "석식"]] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    await interaction.response.defer()
    if school_name:
        results = await school_page(interaction, school_name)
        edu_office_code = results.ATPT_OFCDC_SC_CODE
        standard_school_code = results.SD_SCHUL_CODE
    else:
        user = await interaction.client.orm.get_user(interaction.user.id)
        if not user:
            return await interaction.followup.send("가입되어있지 않은경우 학교명을 입력해주셔야 해요.")
        edu_office_code = user.ATPT_OFCDC_SC_CODE
        standard_school_code = user.SD_SCHUL_CODE

    meal_info = await interaction.client.crenata_neispy.get_meal(
        edu_office_code, standard_school_code, meal_time, date=date
    )

    if not meal_info:
        return await interaction.followup.send(
            "해당 시간에는 급식이 없나봐요! 조식, 중식, 석식중에 다시 선택해주세요!"
        )

    return await interaction.followup.send(meal_info)
