from discord import app_commands
from discord.interactions import Interaction

from crenata.application.client import Crenata
from crenata.application.error.exceptions import MustBeGreaterThanZero
from crenata.application.interaction import major_info_selector, school_page
from crenata.application.strings import ApplicationStrings
from crenata.application.utils import InteractionLock
from crenata.core.majorinfo.usecases.get import GetMajorInfoUseCase
from crenata.core.school.usecases.get import GetSchoolUseCase
from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.core.schoolinfo.usecases.create import CreateSchoolInfoUseCase
from crenata.core.schoolinfo.usecases.update import UpdateSchoolInfoUseCase
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.neispy.majorinfo.domain.repository import (
    MajorInfoRepositoryImpl,
)
from crenata.infrastructure.neispy.school.domain.repository import SchoolRepositoryImpl
from crenata.infrastructure.sqlalchemy.schoolinfo.domain.repository import (
    SchoolInfoRepositoryImpl,
)
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="설정", description="학교를 설정합니다.")
@app_commands.describe(school_name="설정할 학교 이름입니다.")
@app_commands.describe(grade="설정할 학년입니다.")
@app_commands.describe(room="설정할 반입니다.")
async def setup(
    interaction: Interaction[Crenata], school_name: str, grade: int, room: int
) -> None:
    async with InteractionLock(interaction):
        if grade < 1 or room < 1:
            raise MustBeGreaterThanZero

        user_repository = UserRepositoryImpl(interaction.client.database)
        get_user_usecase = GetUserUseCase(user_repository)

        user = await get_user_usecase.execute(interaction.user.id)

        school_repository = SchoolRepositoryImpl(interaction.client.neispy)
        get_school_usecase = GetSchoolUseCase(school_repository)

        schools = await get_school_usecase.execute(school_name)

        school = await school_page(interaction, schools, ephemeral=True)

        school_info = SchoolInfo(
            name=school.name,
            grade=grade,
            room=room,
            edu_office_code=school.edu_office_code,
            standard_school_code=school.standard_school_code,
            department=None,
            major=None,
        )

        if (
            school.highschool_category in ["특목고", "특성화고"]
            and school.highschool_general_or_business != "일반계"
        ):
            major_info_repository = MajorInfoRepositoryImpl(interaction.client.neispy)
            get_major_info_usecase = GetMajorInfoUseCase(major_info_repository)

            major_infos = await get_major_info_usecase.execute(
                school.edu_office_code, school.standard_school_code
            )

            major_info = await major_info_selector(interaction, major_infos)

            school_info.department = major_info.department
            school_info.major = major_info.major

        school_info_repository = SchoolInfoRepositoryImpl(interaction.client.database)

        if user.school_info is None:
            create_school_info_usecase = CreateSchoolInfoUseCase(school_info_repository)
            await create_school_info_usecase.execute(interaction.user.id, school_info)

            await interaction.edit_original_response(
                content=ApplicationStrings.SUCCESSFUL_EDIT, embed=None, view=None
            )

        else:
            update_school_info_usecase = UpdateSchoolInfoUseCase(school_info_repository)
            await update_school_info_usecase.execute(interaction.user.id, school_info)

            await interaction.edit_original_response(
                content=ApplicationStrings.SUCCESSFUL_EDIT, embed=None, view=None
            )
