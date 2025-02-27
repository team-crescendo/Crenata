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
from crenata.application.utils import respond
from crenata.core.meal.exceptions import MealNameNotFound, MealNotFound
from crenata.core.school.exception import SchoolNotFound
from crenata.core.schoolinfo.exceptions import SchoolInfoNotFound
from crenata.core.timetable.exceptions import TimetableNotFound
from crenata.core.user.exceptions import DuplicateUser, UserNotFound

error_handler: ErrorHandler[Crenata] = ErrorHandler()


@error_handler.handle_this_exception(
    DuplicateUser, NotInteractedUser, SchoolInfoNotFound
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
    MealNotFound,
    SchoolNotFound,
)
async def superposition(
    interaction: Interaction[Crenata],
    error: (
        MealNameNotFound
        | UserNotFound
        | TimetableNotFound
        | DateParseError
        | InteractionLocked
        | MustBeGreaterThanZero
        | NeedGradeAndRoomArgument
        | UserCancelled
        | ViewTimeout
        | MealNotFound
        | SchoolNotFound
    ),
) -> None:
    await respond(
        interaction, content=error.message, edit_arg={"embed": None, "view": None}
    )
