"""
유형 힌트에 도움을 주는 파일입니다
"""

from typing import Any, Callable, ParamSpec, TypeVar

from sqlalchemy import Table

from crenata.abc.domain import AbstractDomain
from discord import Embed

T = TypeVar("T")
P = ParamSpec("P")

EmbedMaker = Callable[[Any, int, int], Embed]

DatabaseMapping = list[tuple[type[AbstractDomain], Table, dict[str, Any]]]
