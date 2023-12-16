from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from discord import Colour, Embed
from discord.types.embed import EmbedType


class CrenataEmbed(Embed):
    def __init__(
        self,
        *,
        colour: Optional[int | Colour] = None,
        color: Optional[int | Colour] = 5681003,
        title: Optional[Any] = None,
        type: EmbedType = "rich",
        url: Optional[Any] = None,
        description: Optional[Any] = None,
        timestamp: Optional[datetime] = None,
    ):
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp,
        )

    def apply_page(self, index: int, total: int) -> CrenataEmbed:
        self.set_footer(text=f"{index}/{total}")

        return self
