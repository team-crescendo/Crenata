from datetime import datetime
from typing import Literal, Optional

from discord import app_commands

from crenata.commands.default.meal import Meal
from crenata.typing import CrenataInteraction
from crenata.utils import ToDatetime, defer, use_crenata_command


@app_commands.command(name="급식", description="급식 식단표를 가져와요.")
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(meal_time="시간")
@app_commands.describe(date="날짜")
@use_crenata_command(Meal)
@defer
async def meal(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    meal_time: Optional[Literal["조식", "중식", "석식"]] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    await interaction.execute(school_name, meal_time, date)
