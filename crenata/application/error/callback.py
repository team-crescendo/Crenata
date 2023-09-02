from discord import Interaction

from crenata.application.client import Crenata
from crenata.application.error.handler import ErrorHandler
from crenata.core.user.exceptions import DuplicateUser

error_handler: ErrorHandler[Crenata] = ErrorHandler()


@error_handler.handle_this_exception(DuplicateUser)
async def handle_exception(
    interaction: Interaction[Crenata], error: DuplicateUser
) -> None:
    await interaction.response.send_message(error.message)
