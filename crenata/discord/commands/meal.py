from datetime import datetime
from typing import Literal, Optional

from crenata.commands.meal import Meal
from crenata.discord import CrenataInteraction
from crenata.registry import Registry
from crenata.utils import ToDatetime
from discord import app_commands


@app_commands.command(name="급식", description="급식 식단표를 가져와요.")
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(meal_time="시간")
@app_commands.describe(date="날짜")
async def meal(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    meal_time: Optional[Literal["조식", "중식", "석식"]] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    await Registry.get_command(Meal, interaction).execute(school_name, meal_time, date)
