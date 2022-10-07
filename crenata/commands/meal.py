from typing import Literal, Optional

from discord import app_commands

from crenata.typing import CrenataInteraction


@app_commands.command()  # pyright: ignore [reportGeneralTypeIssues]
async def meal(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    meal_time: Literal["조식", "중식", "석식"] = "중식",
    date: Optional[str] = None,
) -> None:
    if school_name:
        results = await interaction.client.crenata_neispy.search_school(school_name)
        # TODO: Handle school
        raise NotImplementedError
    else:
        user = await interaction.client.orm.get_user(interaction.user.id)
        if not user:
            return await interaction.response.send_message(
                "가입되어있지 않은경우 학교명을 입력해주셔야 해요."
            )
        edu_office_code = user.ATPT_OFCDC_SC_CODE
        standard_school_code = user.SD_SCHUL_CODE

    meal_info = await interaction.client.crenata_neispy.get_meal(
        meal_time, edu_office_code, standard_school_code, date=date
    )

    if not meal_info:
        return await interaction.response.send_message("오늘 날짜의 급식정보는 없는것같아요.")

    return await interaction.response.send_message(meal_info)
