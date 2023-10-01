from crenata.application.client import Crenata
from crenata.application.error.handler import ErrorHandler
from crenata.core.meal.exceptions import MealNameNotFound
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound
from crenata.core.user.exceptions import DuplicateUser
from discord import Interaction

error_handler: ErrorHandler[Crenata] = ErrorHandler()


@error_handler.handle_this_exception(DuplicateUser)
async def duplicate_user(
    interaction: Interaction[Crenata], error: DuplicateUser
) -> None:
    await interaction.response.send_message(error.message)


@error_handler.handle_this_exception(MealNameNotFound)
async def meal_name_not_found(
    interaction: Interaction[Crenata], error: MealNameNotFound
) -> None:
    if interaction.response.is_done():
        await interaction.edit_original_response(
            content=error.message, embed=None, view=None
        )
    else:
        await interaction.response.send_message(error.message)


@error_handler.handle_this_exception(SchoolInfoNotFound)
async def school_info_not_found(
    interaction: Interaction[Crenata], error: SchoolInfoNotFound
) -> None:
    await interaction.response.send_message(error.message)
