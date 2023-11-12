from datetime import datetime
from typing import Optional

from discord import File, app_commands
from discord.interactions import Interaction
from neispy.utils import KST

from crenata.application.client import Crenata
from crenata.application.embeds.timetable import timetable_embed_builder
from crenata.application.error.exceptions import (
    MustBeGreaterThanZero,
    NeedGradeAndRoomArgument,
)
from crenata.application.interaction import school_page
from crenata.application.timetable import make_timetable_image
from crenata.application.utils import ToDatetime
from crenata.core.school.usecases.get import GetSchoolUseCase
from crenata.core.timetable.usecases.get import GetWeekTimetableUseCase
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.neispy.school.domain.repository import SchoolRepositoryImpl
from crenata.infrastructure.neispy.timetable.domain.repository import (
    TimetableRepositoryImpl,
)
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="시간표", description="시간표를 가져옵니다.")
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(grade="학년")
@app_commands.describe(room="반")
@app_commands.describe(date="날짜 (예시: 20230101, 내일)")
async def timetable(
    interaction: Interaction[Crenata],
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    if date is None:
        date = datetime.now(KST)

    if school_name is None:
        user_repository = UserRepositoryImpl(interaction.client.database)
        user = await GetUserUseCase(user_repository).execute(interaction.user.id)
        school_info = user.school_info
        assert school_info

        is_private = user.preferences.private
        ephemeral = user.preferences.ephemeral

        if grade is not None and room is not None:
            if grade < 1 or room < 1:
                raise MustBeGreaterThanZero
        else:
            grade = school_info.grade
            room = school_info.room

    else:
        if grade is None or room is None:
            raise NeedGradeAndRoomArgument

        if grade < 1 or room < 1:
            raise MustBeGreaterThanZero

        school_repository = SchoolRepositoryImpl(interaction.client.neispy)
        school_infos = await GetSchoolUseCase(school_repository).execute(school_name)
        school_info = await school_page(interaction, school_infos)

        is_private = True
        ephemeral = True

    timetable_repository = TimetableRepositoryImpl(interaction.client.neispy)
    timetable_info = await GetWeekTimetableUseCase(timetable_repository).execute(
        school_info.edu_office_code,
        school_info.standard_school_code,
        school_info.name,
        grade,
        room,
        date,
    )

    if not timetable_info:
        await interaction.edit_original_response(
            content="시간표가 없습니다.", embed=None, view=None
        )
        return

    await interaction.edit_original_response(
        content="시간표를 가져오는 중 입니다.", embed=None, view=None
    )

    image = await make_timetable_image(timetable_info, date)
    embed = timetable_embed_builder(school_info.name, date, is_private)

    await interaction.followup.send(
        file=File(image, filename="timetable.png"),
        embed=embed,
        ephemeral=ephemeral,
    )

    await interaction.edit_original_response(content="시간표를 가져왔습니다.")
