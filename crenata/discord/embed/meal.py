from typing import Any, Literal

from crenata.utils.datetime import datetime_to_readable, to_datetime
from crenata.utils.discord import CrenataEmbed, follow_private_preference


def _add_emoji(string: Literal["조식", "중식", "석식"]) -> str:
    """
    조식, 중식, 석식에 맞는 이모지를 추가해주는 함수입니다.
    """
    emoji = {"조식": "⛅", "중식": "☀️", "석식": "🌙"}
    return f"{emoji.get(string, '❓')} {string}"


def _parse_br_tag(string: str) -> str:
    """
    <br/> 태그를 개행문자로 바꿔주는 함수입니다.
    """
    return "\n".join([f"> {word}" for word in string.split("<br/>")])


def meal_embed_builder(results: Any, private: bool) -> CrenataEmbed:
    """
    급식 검색 결과를 Embed로 만들어주는 함수입니다.
    """
    embed = CrenataEmbed()
    embed.set_author(name="🔍 급식 검색 결과")

    for result in results:
        if not embed.title and not embed.description:
            (school_name,) = follow_private_preference(
                private=private, school_name=result.SCHUL_NM
            ).values()

            embed.title = f'"{school_name}" 의 급식 정보'
            embed.description = (
                f"__{datetime_to_readable(to_datetime(result.MLSV_FROM_YMD))}__ 급식"
            )

        embed.add_field(
            name=f"{_add_emoji(result.MMEAL_SC_NM)} ({result.CAL_INFO})",
            value=f"{_parse_br_tag(result.DDISH_NM)}",
            inline=True,
        )

    return embed
