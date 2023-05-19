from datetime import datetime
from typing import Literal, Optional

from crenata.discord import CrenataInteraction
from crenata.discord.commands.school import school
from crenata.discord.embed import allergy_page, meal_page
from crenata.discord.interaction import school_info
from crenata.utils.discord import ToDatetime, dynamic_send
from discord import app_commands, ui


@school.command(name="급식", description="급식 식단표를 가져와요.")
@app_commands.describe(school_name="학교 이름")
@app_commands.describe(meal_time="시간")
@app_commands.describe(date="날짜 (예시: 20230101, 내일)")
async def meal(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    meal_time: Optional[Literal["조식", "중식", "석식"]] = None,
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    info = await school_info(interaction, school_name)

    _, edu_office_code, standard_school_code, preferences = info

    meal_info = meal_page(
        await interaction.client.ctx.neispy.get_meal(
            edu_office_code, standard_school_code, meal_time, date=date
        ),
        private=preferences.private,
    )

    dyn = dynamic_send(interaction)

    if not meal_info:
        await dyn(
            content="해당 시간에는 급식이 없나봐요! 조식, 중식, 석식중에 다시 선택해주세요!",
            embed=None,
            view=None,
            ephemeral=True,
        )
        return

    """async def allergy_callback(interaction):
        await interaction.response.send_message(
            embed=allergy_page(),
            ephemeral=True,
        )"""
    user = interaction.user.id
    async def callback_no_response(interaction):
        if interaction.user.id == user:
            selAllergy.placeholder = selAllergy.values[0]
        await interaction.response.edit_message(view=view)

    view = ui.View()

    lst = []
    selAllergy = ui.Select(placeholder="알러지 정보")
    selAllergy.add_option(label="1.난류, 2.우유, 3.메밀")
    selAllergy.add_option(label="4.땅콩, 5.대두, 6.밀")
    selAllergy.add_option(label="7.고등어, 8.게, 9.새우")
    selAllergy.add_option(label="10.돼지고기, 11.복숭아, 12.토마토")
    selAllergy.add_option(label="13.아황산염, 14.호두, 15.닭고기")
    selAllergy.add_option(label="16.쇠고기, 17.오징어, 18.조개류")
    selAllergy.callback = callback_no_response
    # btnAllergy = ui.Button(label="알러지 내역 확인")
    # btnAllergy.callback = allergy_callback
    view.add_item(selAllergy)

    await dyn(embed=meal_info, ephemeral=preferences.ephemeral, view=view, content=None)
