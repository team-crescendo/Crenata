from datetime import datetime
from typing import Any, Optional

from crenata.abc.command import AbstractCrenataCommand
from crenata.commands.utils import defer
from crenata.discord.interaction import school_page
from crenata.registry import Registry
from crenata.utils import ToDatetime
from discord import app_commands


@Registry.register
class TimeTable(AbstractCrenataCommand):
    @defer
    async def execute(  # pyright: ignore [reportIncompatibleMethodOverride]
        self,
        school_name: Optional[str] = None,
        grade: Optional[int] = None,
        class_num: Optional[int] = None,
        date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
    ) -> Any:
        if school_name:
            if not grade or not class_num:
                await self.respond("학년과 반을 입력해주세요.")
                return
            results = await school_page(self, school_name)
            edu_office_code = results.ATPT_OFCDC_SC_CODE
            standard_school_code = results.SD_SCHUL_CODE
        else:
            user = await self.interaction.client.ctx.orm.get_user(
                self.interaction.user.id
            )
            if not user:
                return await self.respond("가입되어있지 않은경우 학교명을 입력해주셔야 해요.")
            school_name = user.school_name
            edu_office_code = user.ATPT_OFCDC_SC_CODE
            standard_school_code = user.SD_SCHUL_CODE

            if not grade:
                grade = user.grade
            if not class_num:
                class_num = user.class_num

        timetable_info = await self.interaction.client.ctx.neispy.get_time_table(
            edu_office_code,
            standard_school_code,
            school_name,
            grade,
            class_num,
            date=date,
        )

        if not timetable_info:
            return await self.respond("no_time_table")

        return await self.respond(timetable_info)
