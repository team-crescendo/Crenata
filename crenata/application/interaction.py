from discord import Interaction
from discord.ui import Select, View

from crenata.application.client import Crenata
from crenata.application.embeds import CrenataEmbed
from crenata.application.embeds.school import school_embed_builder
from crenata.application.error.exceptions import UserCancelled
from crenata.application.strings import ApplicationStrings
from crenata.application.view.paginator import SelectablePaginator
from crenata.application.view.selector import Selector
from crenata.core.majorinfo.domain.entity import MajorInfo
from crenata.core.school.domain.entity import School


class MajorInfoUI(Select[View]):
    def __init__(self, executor_id: int, major_infos: list[MajorInfo]) -> None:
        self.executor_id = executor_id

        super().__init__(placeholder="학과")

        for n, major_info in enumerate(major_infos, 1):
            value = f"{n}. 계열: {major_info.department} 학과: {major_info.major}"
            self.add_option(
                label=value,
                value=value,
            )

    async def callback(self, interaction: Interaction) -> None:
        if user := interaction.user:
            if user.id == self.executor_id:
                self.placeholder = self.values[0]
                await interaction.response.edit_message(view=self.view)

                return

            await interaction.response.send_message(
                ApplicationStrings.NOT_INTERACTED_USER, ephemeral=True
            )

            return


async def school_page(
    interaction: Interaction[Crenata], schools: list[School], *, ephemeral: bool = False
) -> School:
    """
    학교를 검색하고 선택할 수 있는 페이지를 보여줍니다.
    """

    embeds = [school_embed_builder(school) for school in schools]
    view = SelectablePaginator(interaction.user.id, embeds=embeds)

    await interaction.response.send_message(
        embed=view.embeds[0], view=view, ephemeral=ephemeral
    )

    if not await view.wait():
        if view.is_confirm:
            return schools[view.index]

    raise UserCancelled


async def major_info_selector(
    interaction: Interaction[Crenata], major_infos: list[MajorInfo]
) -> MajorInfo:
    """
    특목고, 특성화고의 경우 학과를 선택할 수 있는 페이지를 보여줍니다.
    """
    major_info_ui = MajorInfoUI(interaction.user.id, major_infos)
    view = Selector(interaction.user.id)
    view.add_item(major_info_ui)

    await interaction.edit_original_response(
        view=view,
        embed=CrenataEmbed(
            title="특성화고 또는 특목고인 것으로 추정됩니다.", description="학과를 선택해 주시길 바랍니다."
        ),
    )

    if not await view.wait():
        if view.is_confirm:
            return major_infos[int(major_info_ui.values[0][0]) - 1]

    raise UserCancelled
