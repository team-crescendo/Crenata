from datetime import datetime, timedelta
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
from crenata.application.interaction import major_info_selector, school_page
from crenata.application.strings import ApplicationStrings
from crenata.application.timetable import make_timetable_image
from crenata.application.utils import ToDatetime, respond
from crenata.core.majorinfo.usecases.get import GetMajorInfoUseCase
from crenata.core.school.usecases.get import GetSchoolUseCase
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound
from crenata.core.strings import CoreStrings
from crenata.core.timetable.usecases.get import GetWeekTimetableUseCase
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.neispy.majorinfo.domain.repository import (
    MajorInfoRepositoryImpl,
)
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
    major: Optional[str] = None,
    department: Optional[str] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    if date is None:
        date = datetime.now(KST)

    if school_name is None:
        user_repository = UserRepositoryImpl(interaction.client.database)
        get_user_usecase = GetUserUseCase(user_repository)

        user = await get_user_usecase.execute(interaction.user.id)

        if user.school_info is None:
            raise SchoolInfoNotFound

        school_info = user.school_info
        is_private = user.preferences.private
        ephemeral = user.preferences.ephemeral
        major = school_info.major
        department = school_info.department

        grade = grade or school_info.grade
        room = room or school_info.room

        if grade < 1 or room < 1:
            raise MustBeGreaterThanZero

    else:
        if grade is None or room is None:
            raise NeedGradeAndRoomArgument

        if grade < 1 or room < 1:
            raise MustBeGreaterThanZero

        school_repository = SchoolRepositoryImpl(interaction.client.neispy)
        get_school_usecase = GetSchoolUseCase(school_repository)

        school_infos = await get_school_usecase.execute(school_name)

        school_info = await school_page(interaction, school_infos)

        is_private = True
        ephemeral = True

        if (
            school_info.highschool_category in ["특목고", "특성화고"]
            and school_info.highschool_general_or_business != "일반계"
        ):
            major_info_repository = MajorInfoRepositoryImpl(interaction.client.neispy)
            get_major_info_usecase = GetMajorInfoUseCase(major_info_repository)

            major_infos = await get_major_info_usecase.execute(
                school_info.edu_office_code, school_info.standard_school_code
            )

            major_info = await major_info_selector(interaction, major_infos)

            major = major_info.major
            department = major_info.department

    dates = [
        date + timedelta(days=i) for i in range(-date.weekday(), 5 - date.weekday())
    ]

    timetable_repository = TimetableRepositoryImpl(interaction.client.neispy)
    get_week_timetable_usecase = GetWeekTimetableUseCase(timetable_repository)

    timetable_info = await get_week_timetable_usecase.execute(
        school_info.edu_office_code,
        school_info.standard_school_code,
        school_info.name,
        grade,
        room,
        dates,
        major,
        department,
    )

    if not timetable_info:
        await respond(
            interaction,
            content=CoreStrings.TIMETABLE_NOT_FOUND,
            edit_arg={"embed": None, "view": None},
        )

        return

    await respond(
        interaction,
        content=ApplicationStrings.TIMETABLE_LOADING,
        edit_arg={"embed": None, "view": None},
    )

    image = await make_timetable_image(timetable_info, date)

    embed = timetable_embed_builder(school_info.name, dates, is_private)

    await interaction.followup.send(
        file=File(image, filename="timetable.png"), embed=embed, ephemeral=ephemeral
    )

    await interaction.edit_original_response(
        content=ApplicationStrings.TIMETABLE_LOADED
    )
