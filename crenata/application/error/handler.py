from typing import Any, Callable, Coroutine


class ErrorHandler:
    def __init__(self) -> None:
        self.__mapping: dict[
            type[Exception], Callable[..., Coroutine[Any, Any, Any]]
        ] = {}

    def callback(self, error: Exception):
        callback = self.__mapping.get(type(error))
        if callback:
            return callback(error)

    def handle_this_exception(self, error_type: type[Exception]):
        def decorator(callback: Callable[..., Coroutine[Any, Any, Any]]):
            self.__mapping[error_type] = callback
            return callback

        return decorator
