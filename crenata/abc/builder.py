from __future__ import annotations
from typing import Any
from discord import Embed
from abc import ABC


class AbstractEmbedBuilder(ABC):
    def __init__(self) -> None:
        self.embed = Embed(color=5681003)

    def apply_private_preference(self, private: bool) -> AbstractEmbedBuilder:
        self.private = private
        return self

    def apply_pagination(self, index: int, total: int) -> AbstractEmbedBuilder:
        self.embed.set_footer(text=f"{index}/{total}")
        return self

    def build(self, data: Any) -> Embed:
        ...

    @classmethod
    def with_apply_pagination(
        cls, index: int = 1, total: int = 1
    ) -> AbstractEmbedBuilder:
        return cls().apply_pagination(index, total)

    @classmethod
    def with_apply_private_preference(cls, private: bool) -> AbstractEmbedBuilder:
        return cls().apply_private_preference(private)
