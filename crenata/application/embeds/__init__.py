from datetime import datetime
from typing import Any

from discord import Colour, Embed
from discord.types.embed import EmbedType


class CrenataEmbed(Embed):
    def __init__(
        self,
        *,
        colour: int | Colour | None = None,
        color: int | Colour | None = 5681003,
        title: Any | None = None,
        type: EmbedType = "rich",
        url: Any | None = None,
        description: Any | None = None,
        timestamp: datetime | None = None,
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

    def apply_page(self, index: int, total: int) -> None:
        self.set_footer(text=f"{index}/{total}")
