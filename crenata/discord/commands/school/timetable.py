from datetime import datetime
from typing import Optional

from crenata.discord import CrenataInteraction
from crenata.discord.commands.school import school
from crenata.discord.embed.timetable import timetable_embed_builder
from crenata.discord.interaction import school_info
from crenata.discord.timetable import make_timetable_image
from crenata.utils.discord import ToDatetime, dynamic_send
from discord import File, app_commands


@school.command(name="시간표", description="시간표를 가져와요.")
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(grade="학년")
@app_commands.describe(room="반")
@app_commands.describe(date="날짜 (예시: 20230101, 내일)")
async def time_table(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    info = await school_info(interaction, school_name, grade, room, handle_detail=True)

    school_name, edu_office_code, standard_school_code, grade, room, preferences = info

    timetable_info, date = await interaction.client.ctx.neispy.get_week_time_table(
        edu_office_code,
        standard_school_code,
        school_name,
        grade,
        room,
        date=date,
    )

    dyn = dynamic_send(interaction)

    if not timetable_info:
        await dyn(content="시간표가 없어요.", embed=None, view=None)
        return

    await dyn(content="시간표를 가져오는 중이에요...", embed=None, view=None)

    image = await make_timetable_image(timetable_info, date)
    embed = timetable_embed_builder(timetable_info, date, preferences.private)

    await dyn(
        followup=True,
        file=File(image, filename="timetable.png"),
        embed=embed,
        ephemeral=preferences.ephemeral,
    )

    await dyn(content="시간표를 가져왔어요!")
