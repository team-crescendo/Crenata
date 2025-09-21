from datetime import datetime
from typing import Literal, Optional

from discord import app_commands, ui
from discord.interactions import Interaction
from neispy.utils import KST

from crenata.application.client import Crenata
from crenata.application.embeds.meal import meal_embed_builder
from crenata.application.interaction import school_page
from crenata.application.utils import ToDatetime, respond
from crenata.core.meal.exceptions import MealNameNotFound
from crenata.core.meal.usecases.get import GetMealUseCase
from crenata.core.school.usecases.get import GetSchoolUseCase
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound
from crenata.core.user.usecases.get import GetUserUseCase
from crenata.infrastructure.neispy.meal.domain.repository import MealRepositoryImpl
from crenata.infrastructure.neispy.school.domain.repository import SchoolRepositoryImpl
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


class AllergyUI(ui.Select[ui.View]):
    def __init__(self, executor_id: int) -> None:
        super().__init__(placeholder="알러지 정보")
        self.executor_id = executor_id
        self.add_option(label="1.난류, 2.우유, 3.메밀")
        self.add_option(label="4.땅콩, 5.대두, 6.밀")
        self.add_option(label="7.고등어, 8.게, 9.새우")
        self.add_option(label="10.돼지고기, 11.복숭아, 12.토마토")
        self.add_option(label="13.아황산염, 14.호두, 15.닭고기")
        self.add_option(label="16.쇠고기, 17.오징어, 18.조개류")

    async def callback(self, interaction: Interaction) -> None:
        if self.executor_id == interaction.user.id:
            self.placeholder = self.values[0]
            await interaction.response.edit_message(view=self.view)


@app_commands.command(name="급식", description="급식 식단표를 가져옵니다.")
async def meal(
    interaction: Interaction[Crenata],
    school_name: Optional[str] = None,
    meal_time: Literal["조식", "중식", "석식", "아침", "점심", "저녁"] = "중식",
    date: Optional[app_commands.Transform[datetime, ToDatetime]] = None,
) -> None:
    convert_table = {
        "아침": "조식",
        "점심": "중식",
        "저녁": "석식",
    }
    if date is None:
        date = datetime.now(tz=KST)

    if meal_time in convert_table:
        meal_time = convert_table[meal_time]

    if school_name is None:
        user_repository = UserRepositoryImpl(interaction.client.database)
        get_user_usecase = GetUserUseCase(user_repository)

        user = await get_user_usecase.execute(interaction.user.id)

        if user.school_info is None:
            raise SchoolInfoNotFound

        school_info = user.school_info
        is_private = user.preferences.private

    else:
        school_repository = SchoolRepositoryImpl(interaction.client.neispy)
        get_school_usecase = GetSchoolUseCase(school_repository)

        school_infos = await get_school_usecase.execute(school_name)

        school_info = await school_page(interaction, school_infos)

        is_private = True

    meal_repository = MealRepositoryImpl(interaction.client.neispy)
    get_meal_usecase = GetMealUseCase(meal_repository)

    meal = await get_meal_usecase.execute(
        school_info.edu_office_code, school_info.standard_school_code, date, meal_time
    )

    if not meal:
        raise MealNameNotFound

    embed = meal_embed_builder(meal, is_private)

    view = ui.View()
    select_allergy_ui = AllergyUI(interaction.user.id)
    view.add_item(select_allergy_ui)

    await respond(interaction, content=None, embed=embed, view=view)
