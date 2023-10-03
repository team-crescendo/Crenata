from discord import Interaction

from crenata.application.client import Crenata
from crenata.application.error.handler import ErrorHandler
from crenata.core.meal.exceptions import MealNameNotFound
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound
from crenata.core.user.exceptions import DuplicateUser

error_handler: ErrorHandler[Crenata] = ErrorHandler()


@error_handler.handle_this_exception(DuplicateUser, SchoolInfoNotFound)
async def confirmed(
    interaction: Interaction[Crenata], error: DuplicateUser | SchoolInfoNotFound
) -> None:
    await interaction.response.send_message(error.message)


@error_handler.handle_this_exception(MealNameNotFound)
async def superposition(
    interaction: Interaction[Crenata], error: MealNameNotFound
) -> None:
    if interaction.response.is_done():
        await interaction.edit_original_response(
            content=error.message, embed=None, view=None
        )
    else:
        await interaction.response.send_message(error.message)
