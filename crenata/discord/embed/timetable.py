from typing import Any

from crenata.abc.builder import AbstractEmbedBuilder
from crenata.utils.datetime import datetime_to_readable
from discord import Embed


class TimetableEmbedBuilder(AbstractEmbedBuilder):
    def build(self, *data: Any) -> Embed:
        results, date = data
        r = results[0][0]

        school_name = self.follow_private_preference(r.SCHUL_NM)

        self.embed.title = "🗓️ 시간표"
        self.embed.description = f"{school_name} __{datetime_to_readable(date)}__ 시간표"
        self.embed.set_image(url="attachment://timetable.png")

        return self.embed
