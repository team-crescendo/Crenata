from datetime import datetime
from typing import Optional

from discord import app_commands

from crenata.commands.default.timetable import TimeTable
from crenata.typing import CrenataInteraction
from crenata.utils import ToDatetime, defer, use_crenata_command


@app_commands.command(name="시간표", description="시간표를 가져와요.")
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(grade="학년")
@app_commands.describe(class_num="반")
@app_commands.describe(date="날짜")
@use_crenata_command(TimeTable)
@defer
async def time_table(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    class_num: Optional[int] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    await interaction.execute(school_name, grade, class_num, date)
