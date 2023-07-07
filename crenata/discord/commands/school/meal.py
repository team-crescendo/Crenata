from datetime import datetime
from typing import Literal, Optional

from crenata.discord import CrenataInteraction
from crenata.discord.commands.school import school
from crenata.discord.embed.meal import meal_embed_builder
from crenata.discord.interaction import school_info
from crenata.utils.discord import ToDatetime, dynamic_send
from discord import app_commands, ui
from discord.interactions import Interaction


class AllergyUI(ui.Select[ui.View]):
    def __init__(self, executor_id: int) -> None:
        super().__init__(placeholder="알러지 정보")
        self.executor_id = executor_id
        self.add_option(label="4.땅콩, 5.대두, 6.밀")
        self.add_option(label="1.난류, 2.우유, 3.메밀")
        self.add_option(label="7.고등어, 8.게, 9.새우")
        self.add_option(label="10.돼지고기, 11.복숭아, 12.토마토")
        self.add_option(label="13.아황산염, 14.호두, 15.닭고기")
        self.add_option(label="16.쇠고기, 17.오징어, 18.조개류")

    async def callback(self, interaction: Interaction) -> None:
        if self.executor_id == interaction.user.id:
            self.placeholder = self.values[0]
            await interaction.response.edit_message(view=self.view)


@school.command(name="급식", description="급식 식단표를 가져와요.")  # type: ignore[arg-type]
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(meal_time="시간")
@app_commands.describe(date="날짜 (예시: 20230101, 내일)")
async def meal(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    meal_time: Optional[Literal["조식", "중식", "석식"]] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    dyn = dynamic_send(interaction)

    info = await school_info(interaction, school_name)

    _, edu_office_code, standard_school_code, preferences = info

    data = await interaction.client.ctx.neispy.get_meal(
        edu_office_code, standard_school_code, meal_time, date=date
    )

    if not data:
        await dyn(
            content="해당 시간에는 급식이 없나봐요! 조식, 중식, 석식중에 다시 선택해주세요!",
            embed=None,
            view=None,
            ephemeral=True,
        )
        return

    embed = meal_embed_builder(data, preferences.private)

    view = ui.View()
    select_allergy_ui = AllergyUI(interaction.user.id)
    view.add_item(select_allergy_ui)

    await dyn(embed=embed, ephemeral=preferences.ephemeral, view=view, content=None)
