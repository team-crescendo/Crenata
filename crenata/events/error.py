from traceback import format_exception

import discord
from discord import TextChannel, app_commands


def joined_format_exception(error: BaseException):
    return "".join(format_exception(type(error), error, error.__traceback__))


async def on_error(
    interaction: discord.Interaction, error: app_commands.AppCommandError
) -> None:
    if isinstance(interaction.channel, TextChannel):
        if error.__cause__:
            await interaction.channel.send(
                content=f"```{joined_format_exception(error.__cause__)}```"
            )
            return None
        await interaction.channel.send(
            content=f"```{joined_format_exception(error)}```"
        )
