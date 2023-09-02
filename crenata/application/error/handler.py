from typing import TYPE_CHECKING, Any, Callable, Coroutine, Generic, ParamSpec, TypeVar

from discord import Interaction
from discord._types import ClientT

P = ParamSpec("P")

if TYPE_CHECKING:
    Error = TypeVar("Error", bound=BaseException, default=BaseException)
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

    def handle_this_exception(self, error_type: type[Error]):
        def decorator(
            callback: Callable[[Interaction[ClientT], Error], Coroutine[Any, Any, None]]
        ):
            self.mapped_handlers[error_type] = callback
            return callback

        return decorator
