from typing import Any

from crenata.embed import school_result_embed_maker
from crenata.exception import UserCanceled, ViewTimeout
from crenata.paginator import Paginator
from crenata.typing import CrenataInteraction


async def school_page(interaction: CrenataInteraction, school_name: str) -> Any:
    results = await interaction.client.crenata_neispy.search_school(school_name)
    view = Paginator(interaction.user.id, results, school_result_embed_maker)

    await interaction.followup.send(embed=view.embeds[0], view=view)

    if not await view.wait():
        if view.selected:
            data = view.data[view.index]
            return data

        raise UserCanceled

    raise ViewTimeout
