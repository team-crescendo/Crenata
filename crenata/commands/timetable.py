from typing import Optional

from discord import app_commands

from crenata.interaction import school_page
from crenata.typing import CrenataInteraction


@app_commands.command(
    name="시간표", description="시간표를 가져와요."
)  # pyright: ignore [reportGeneralTypeIssues]
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(grade="학년")
@app_commands.describe(class_num="반")
@app_commands.describe(date="날짜")
async def time_table(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    class_num: Optional[int] = None,
    date: Optional[str] = None,
) -> None:
    await interaction.response.defer()
    if school_name:
        if not grade or not class_num:
            await interaction.followup.send("학년과 반을 입력해주세요.")
            return
        results = await school_page(interaction, school_name)
        edu_office_code = results.ATPT_OFCDC_SC_CODE
        standard_school_code = results.SD_SCHUL_CODE
    else:
        user = await interaction.client.orm.get_user(interaction.user.id)
        if not user:
            return await interaction.followup.send("가입되어있지 않은경우 학교명을 입력해주셔야 해요.")
        school_name = user.school_name
        edu_office_code = user.ATPT_OFCDC_SC_CODE
        standard_school_code = user.SD_SCHUL_CODE

        if not grade:
            grade = user.grade
        if not class_num:
            class_num = user.class_num

    timetable_info = await interaction.client.crenata_neispy.get_time_table(
        edu_office_code, standard_school_code, school_name, grade, class_num, date=date
    )

    if not timetable_info:
        return await interaction.followup.send("no_time_table")

    return await interaction.followup.send(timetable_info)
