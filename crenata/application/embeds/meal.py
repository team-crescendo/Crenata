from crenata.application.embeds import CrenataEmbed
from crenata.application.utils import follow_private_preference
from crenata.core.meal.domain.entity import Meal
from crenata.infrastructure.utils.datetime import datetime_to_readable


def _add_emoji(string: str) -> str:
    """
    조식, 중식, 석식에 맞는 이모지를 추가해 주는 함수입니다.
    """
    emoji = {"조식": "⛅", "중식": "☀️", "석식": "🌙"}

    return f"{emoji.get(string, '❓')} {string}"


def _parse_br_tag(string: str) -> str:
    """
    <br/> 태그를 개행문자로 바꿔주는 함수입니다.
    """
    return "\n".join([f"> {word}" for word in string.split("<br/>")])


def meal_embed_builder(meals: list[Meal], is_private: bool) -> CrenataEmbed:
    """
    급식 검색 결과를 Embed로 만들어 주는 함수입니다.
    """
    embed = CrenataEmbed()

    embed.set_author(name="🔍 급식 검색 결과")

    for meal in meals:
        if not embed.title and not embed.description:
            (school_name,) = follow_private_preference(
                is_private, school_name=meal.school_name
            )

            embed.title = f'"{school_name}" 의 급식 정보'
            embed.description = f"__{datetime_to_readable(meal.date)}__ 급식"

        embed.add_field(
            name=f"{_add_emoji(meal.name)} ({meal.calorie})",
            value=f"{_parse_br_tag(meal.dish_name)}",
            inline=True,
        )

    return embed
