from contextlib import suppress
from functools import partial
from traceback import format_exception

from crenata.discord import CrenataInteraction
from crenata.exception import *
from crenata.utils.discord import dynamic_send
from discord import TextChannel, app_commands
from discord.errors import InteractionResponded
from neispy.error import DataNotFound


def joined_format_exception(error: BaseException) -> str:
    return "".join(format_exception(type(error), error, error.__traceback__))


async def on_error(
    interaction: CrenataInteraction, error: app_commands.AppCommandError
) -> None:
    if original_exception := error.__cause__:
        send = partial(dynamic_send(interaction), followup=True)
        if isinstance(original_exception, DataNotFound):
            with suppress(InteractionResponded):
                await interaction.response.defer(ephemeral=True)
            await send(content="해당하는 정보를 찾을수 없었어요.", embed=None, view=None)

        elif isinstance(original_exception, CrenataException):
            send = partial(send, content=original_exception.__doc__)
            if original_exception.edit:
                await send(embed=None, view=None)
                return

            await interaction.response.defer(ephemeral=True)
            await send()
        # NOTE: for debug
        else:
            if (
                isinstance(interaction.channel, TextChannel)
                and not interaction.client.ctx.config.PRODUCTION
            ):
                await interaction.channel.send(
                    content=f"```{joined_format_exception(original_exception)}```"
                )
