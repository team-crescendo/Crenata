"""
유형 힌트에 도움을 주는 파일입니다
"""

from typing import Any, Callable

from discord import Embed, Interaction

from crenata.client import Crenata


class CrenataInteraction(Interaction):
    @property
    def client(self) -> Crenata:
        ...


EmbedMaker = Callable[[Any, int, int], Embed]
