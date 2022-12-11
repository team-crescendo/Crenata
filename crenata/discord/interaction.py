from typing import Any

from crenata.abc.command import AbstractCrenataCommand
from crenata.discord.embed import school_result_embed_maker
from crenata.discord.paginator import Paginator
from crenata.exception import UserCanceled, ViewTimeout


async def school_page(command: AbstractCrenataCommand, school_name: str) -> Any:
    results = await command.interaction.client.ctx.neispy.search_school(school_name)
    view = Paginator(command.interaction.user.id, results, school_result_embed_maker)

    await command.respond(embed=view.embeds[0], view=view)

    if not await view.wait():
        if view.selected:
            data = view.data[view.index]
            return data

        raise UserCanceled

    raise ViewTimeout
