from typing import TYPE_CHECKING, Any, Callable, Coroutine, Generic, Optional, TypeVar

from discord import Interaction
from discord._types import ClientT

if TYPE_CHECKING:
    Error = TypeVar(
        "Error", bound=BaseException, default=BaseException  # pyright: ignore
    )
else:
    Error = TypeVar("Error", bound=BaseException)


class ErrorHandler(Generic[ClientT]):
    def __init__(self) -> None:
        self.mapped_handlers: dict[
            type[BaseException],
            Callable[..., Coroutine[Any, Any, None]],
        ] = {}

    def lookup(
        self, error: Error
    ) -> Optional[Callable[[Interaction[ClientT], Error], Coroutine[Any, Any, None]]]:
        exception_class = type(error)

        return self.mapped_handlers.get(exception_class)

    def handle_this_exception(
        self, *error_types: type[Error]
    ) -> Callable[
        [Callable[[Interaction[ClientT], Error], Coroutine[Any, Any, None]]],
        Callable[[Interaction[ClientT], Error], Coroutine[Any, Any, None]],
    ]:
        def decorator(
            callback: Callable[[Interaction[ClientT], Error], Coroutine[Any, Any, None]]
        ) -> Callable[[Interaction[ClientT], Error], Coroutine[Any, Any, None]]:
            for error_type in error_types:
                self.mapped_handlers[error_type] = callback

            return callback

        return decorator

    async def on_error(self, interaction: Interaction[ClientT], error: Error) -> None:
        err = error.__cause__ or error

        if callback := self.lookup(err):
            return await callback(interaction, err)

        raise err
