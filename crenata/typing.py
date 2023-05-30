"""
유형 힌트에 도움을 주는 파일입니다
"""

from typing import Any, Coroutine, ParamSpec, Protocol, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


class InnerSend(Protocol):
    def __call__(
        self, *, followup: bool = False, **kwargs: Any
    ) -> Coroutine[Any, Any, None]:
        """
        인터랙션의 원래 메시지가 존재하면 수정하고, 존재하지 않으면 메시지를 보냅니다.

        의도하지 않은 결과를 초래할 수 있으므로 신중히 사용해야 합니다.
        """
        ...
