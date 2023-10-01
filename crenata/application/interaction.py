from discord import Interaction

from crenata.application.client import Crenata
from crenata.application.embeds.school import school_embed_builder
from crenata.application.error.exceptions import UserCancelled
from crenata.application.view.paginator import SelectablePaginator
from crenata.core.school.domain.entity import School


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
