from datetime import datetime

from crenata.application.embeds import CrenataEmbed
from crenata.application.utils import follow_private_preference
from crenata.infrastructure.utils.datetime import datetime_to_readable


def timetable_embed_builder(
    school_name: str, date: list[datetime], private: bool
) -> CrenataEmbed:
    embed = CrenataEmbed()

    (school_name,) = follow_private_preference(private, school_name=school_name)

    embed.title = "🗓️ 시간표"
    embed.description = (
        f"{school_name} __{datetime_to_readable(date[0])} ~"
        f" {datetime_to_readable(date[-1])}__ 시간표"
    )
    embed.set_image(url="attachment://timetable.png")

    return embed
