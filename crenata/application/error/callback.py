from discord import Interaction

from crenata.application.client import Crenata
from crenata.application.error.exceptions import (
    DateParseError,
    InteractionLocked,
    MustBeGreaterThanZero,
    NeedGradeAndRoomArgument,
    NotInteractedUser,
    UserCancelled,
    ViewTimeout,
)
from crenata.application.error.handler import ErrorHandler
from crenata.core.meal.exceptions import MealNameNotFound
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound
from crenata.core.timetable.exceptions import TimetableNotFound
from crenata.core.user.exceptions import DuplicateUser, UserNotFound

error_handler: ErrorHandler[Crenata] = ErrorHandler()


@error_handler.handle_this_exception(
    DuplicateUser,
    NotInteractedUser,
    SchoolInfoNotFound,
)
async def confirmed(
    interaction: Interaction[Crenata],
    error: DuplicateUser | SchoolInfoNotFound | NotInteractedUser,
) -> None:
    await interaction.response.send_message(error.message)


@error_handler.handle_this_exception(
    MealNameNotFound,
    UserNotFound,
    TimetableNotFound,
    DateParseError,
    InteractionLocked,
    MustBeGreaterThanZero,
    NeedGradeAndRoomArgument,
    UserCancelled,
    ViewTimeout,
)
async def superposition(
    interaction: Interaction[Crenata],
    error: MealNameNotFound
    | UserNotFound
    | TimetableNotFound
    | DateParseError
    | InteractionLocked
    | MustBeGreaterThanZero
    | NeedGradeAndRoomArgument
    | UserCancelled
    | ViewTimeout,
) -> None:
    if interaction.response.is_done():
        await interaction.edit_original_response(
            content=error.message, embed=None, view=None
        )
    else:
        await interaction.response.send_message(error.message)
