from datetime import datetime
from typing import Any

from crenata.utils.datetime import datetime_to_readable
from crenata.utils.discord import follow_private_preference, CrenataEmbed


def timetable_embed_builder(
    results: Any, date: datetime, private: bool
) -> CrenataEmbed:
    embed = CrenataEmbed()
    r = results[0][0]

    (school_name,) = follow_private_preference(
        private=private,
        school_name=r.SCHUL_NM,
    ).values()

    embed.title = "🗓️ 시간표"
    embed.description = f"{school_name} __{datetime_to_readable(date)}__ 시간표"
    embed.set_image(url="attachment://timetable.png")

    return embed
