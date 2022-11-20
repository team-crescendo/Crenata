from traceback import format_exception

from discord import NotFound, TextChannel, app_commands
from neispy.error import DataNotFound

from crenata.exception import UserCanceled, ViewTimeout
from crenata.typing import CrenataInteraction


def joined_format_exception(error: BaseException) -> str:
    return "".join(format_exception(type(error), error, error.__traceback__))


async def on_error(
    interaction: CrenataInteraction, error: app_commands.AppCommandError
) -> None:
    if original_exception := error.__cause__:
        if isinstance(original_exception, DataNotFound):
            try:
                message = await interaction.original_response()
            except NotFound:
                await interaction.followup.send("해당하는 정보를 찾을수 없었어요.")
            else:
                await message.edit(content="해당하는 정보를 찾을수 없었어요.", embed=None, view=None)

        elif isinstance(original_exception, UserCanceled):
            await interaction.edit_original_response(
                content="취소했어요 :(", embed=None, view=None
            )
            return
        elif isinstance(original_exception, ViewTimeout):
            await interaction.edit_original_response(
                content="시간이 초과되었어요.", embed=None, view=None
            )
            return
        elif isinstance(original_exception, ValueError):
            await interaction.response.send_message(
                "날짜를 잘못 입력한것 같아요. YYYYMMDD 형식으로 입력해주세요. 예: 20220110"
            )
        # NOTE: for debug
        else:
            if (
                isinstance(interaction.channel, TextChannel)
                and not interaction.client.config.PRODUCTION
            ):
                await interaction.channel.send(
                    content=f"```{joined_format_exception(original_exception)}```"
                )
