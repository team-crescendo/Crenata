from typing import Any

from crenata.discord import CrenataInteraction
from crenata.discord.embed import school_result_embed_maker
from crenata.discord.paginator import Paginator
from crenata.exception import UserCanceled, ViewTimeout


async def school_page(interaction: CrenataInteraction, school_name: str) -> Any:
    results = await interaction.client.ctx.neispy.search_school(school_name)
    view = Paginator(interaction.user.id, results, school_result_embed_maker)

    await interaction.followup.send(embed=view.embeds[0], view=view)

    if not await view.wait():
        if view.selected:
            data = view.data[view.index]
            return data

        raise UserCanceled

    raise ViewTimeout