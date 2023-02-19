from datetime import datetime
from typing import Literal, Optional

from crenata.discord import CrenataInteraction
from crenata.discord.commands.school import school
from crenata.discord.embed import meal_page
from crenata.discord.interaction import school_info
from crenata.utils.discord import ToDatetime, dynamic_send
from discord import app_commands


@school.command(name="급식", description="급식 식단표를 가져와요.")
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(meal_time="시간")
@app_commands.describe(date="날짜 (예시: 20230101, 내일)")
async def meal(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    meal_time: Optional[Literal["조식", "중식", "석식"]] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    info = await school_info(interaction, school_name)

    _, edu_office_code, standard_school_code, preferences = info

    meal_info = meal_page(
        await interaction.client.ctx.neispy.get_meal(
            edu_office_code, standard_school_code, meal_time, date=date
        ),
        private=preferences.private,
    )

    dyn = dynamic_send(interaction)

    if not meal_info:
        await dyn(
            content="해당 시간에는 급식이 없나봐요! 조식, 중식, 석식중에 다시 선택해주세요!",
            embed=None,
            view=None,
            ephemeral=True,
        )
        return

    await dyn(embed=meal_info, ephemeral=preferences.ephemeral, view=None, content=None)
