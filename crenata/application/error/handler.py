from typing import TYPE_CHECKING, Any, Callable, Coroutine, Generic, TypeVar

from discord._types import ClientT

from discord import Interaction

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
    ) -> Callable[[Interaction[ClientT], Error], Coroutine[Any, Any, None]] | None:
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

        callback = self.lookup(err)
        if callback:
            return await callback(interaction, err)

        raise err
