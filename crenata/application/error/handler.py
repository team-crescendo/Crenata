from typing import Any, Callable, Coroutine, Generic

from discord import Interaction
from discord._types import ClientT


class ErrorHandler(Generic[ClientT]):
    def __init__(self) -> None:
        self.__mapping: dict[
            type[Exception],
            Callable[[Interaction[ClientT], Exception], Coroutine[Any, Any, Any]],
        ] = {}

    def callback(self, interaction: Interaction[ClientT], error: Exception):
        callback = self.__mapping.get(type(error))
        if callback:
            return callback(interaction, error)

    def handle_this_exception(self, *error_types: type[Exception]):
        def decorator(
            callback: Callable[
                [Interaction[ClientT], Exception], Coroutine[Any, Any, Any]
            ]
        ):
            for error_type in error_types:
                self.__mapping[error_type] = callback
            return callback

        return decorator
