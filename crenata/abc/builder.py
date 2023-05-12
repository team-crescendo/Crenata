from typing import Any
from discord import Embed
from abc import ABC


class AbstractEmbedBuilder(ABC):
    def __init__(self) -> None:
        self.embed = Embed(color=5681003)

    def apply_private_preference(self, private: bool) -> None:
        self.private = private

    def _build(self, data: Any):
        ...

    @classmethod
    def build(cls, data: Any):
        instance = cls()
        instance._build(data)
        return instance.embed

    @classmethod
    def build_with_apply_private_preference(cls, data: Any, private: bool):
        instance = cls()
        instance.apply_private_preference(private)
        instance._build(data)
        return instance.embed
