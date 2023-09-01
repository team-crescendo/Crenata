from discord import Interaction

from crenata.application.client import Crenata
from crenata.application.error.handler import ErrorHandler

error_handler: ErrorHandler[Crenata] = ErrorHandler()


@error_handler.handle_this_exception(Exception)
async def handle_exception(interaction: Interaction[Crenata], error: Exception) -> None:
    await interaction.response.send_message(f"```py\n{error}\n```")
