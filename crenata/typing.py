"""
유형 힌트에 도움을 주는 파일입니다
"""

from discord import Interaction

from crenata.client import Crenata


class CrenataInteraction(Interaction):
    @property
    def client(self) -> Crenata:
        ...
