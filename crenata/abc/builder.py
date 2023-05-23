from __future__ import annotations

from abc import ABC
from typing import Any

from discord import Embed


class AbstractEmbedBuilder(ABC):
    def __init__(self) -> None:
        self.embed = Embed(color=5681003)

    def follow_private_preference(self, school_name: str) -> str:
        if self.private:
            school_name = "비공개"
        return school_name

    def apply_private_preference(self, private: bool) -> AbstractEmbedBuilder:
        self.private = private
        return self

    def apply_pagination(self, index: int, total: int) -> AbstractEmbedBuilder:
        self.embed.set_footer(text=f"{index}/{total}")
        return self

    def build(self, *data: Any) -> Embed:
        ...

    @classmethod
    def with_apply_pagination(
        cls, index: int = 1, total: int = 1
    ) -> AbstractEmbedBuilder:
        return cls().apply_pagination(index, total)

    @classmethod
    def with_apply_private_preference(cls, private: bool) -> AbstractEmbedBuilder:
        return cls().apply_private_preference(private)

    @classmethod
    def quick_build(cls, *data: Any) -> Embed:
        return cls().build(data)
