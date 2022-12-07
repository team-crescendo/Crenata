from datetime import datetime
from typing import Literal, Optional

from crenata.abc.command import AbstractCrenataCommand
from crenata.discord import CrenataInteraction
from crenata.discord.interaction import school_page
from crenata.utils import ToDatetime
from discord import app_commands
from crenata.commands.utils import defer

class Meal(AbstractCrenataCommand):
    interaction: CrenataInteraction

    @defer
    async def execute(  # pyright: ignore [reportIncompatibleMethodOverride]
        self,
        school_name: Optional[str] = None,
        meal_time: Optional[Literal["조식", "중식", "석식"]] = None,
        date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
    ) -> None:
        if school_name:
            results = await school_page(self.interaction, school_name)
            edu_office_code = results.ATPT_OFCDC_SC_CODE
            standard_school_code = results.SD_SCHUL_CODE
        else:
            user = await self.interaction.client.ctx.orm.get_user(
                self.interaction.user.id
            )
            if not user:
                return await self.interaction.followup.send(
                    "가입되어있지 않은경우 학교명을 입력해주셔야 해요."
                )
            edu_office_code = user.ATPT_OFCDC_SC_CODE
            standard_school_code = user.SD_SCHUL_CODE

        meal_info = await self.interaction.client.ctx.neispy.get_meal(
            edu_office_code, standard_school_code, meal_time, date=date
        )

        if not meal_info:
            return await self.interaction.followup.send(
                "해당 시간에는 급식이 없나봐요! 조식, 중식, 석식중에 다시 선택해주세요!"
            )

        return await self.interaction.followup.send(meal_info)
