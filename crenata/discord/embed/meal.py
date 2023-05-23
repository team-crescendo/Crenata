from typing import Any, Literal
from discord import Embed
from crenata.abc.builder import AbstractEmbedBuilder
from crenata.utils.datetime import datetime_to_readable, to_datetime


class MealEmbedBuilder(AbstractEmbedBuilder):
    def add_emoji(self, string: Literal["조식", "중식", "석식"]) -> str:
        """
        조식, 중식, 석식에 맞는 이모지를 추가해주는 함수입니다.
        """
        emoji = {"조식": "⛅", "중식": "☀️", "석식": "🌙"}
        return f"{emoji.get(string, '❓')} {string}"

    def parse_br_tag(self, string: str) -> str:
        """
        <br/> 태그를 개행문자로 바꿔주는 함수입니다.
        """
        return "\n".join([f"> {word}" for word in string.split("<br/>")])


    def build(self, *data: Any) -> Embed:
        """
        급식 검색 결과를 Embed로 만들어주는 함수입니다.
        """
        self.embed.set_author(name="🔍 급식 검색 결과")

        for result in data[0]:
            if not self.embed.title and not self.embed.description:
                school_name = self.follow_private_preference(result.SCHUL_NM)

                self.embed.title = f'"{school_name}" 의 급식 정보'
                self.embed.description = (
                    f"__{datetime_to_readable(to_datetime(result.MLSV_FROM_YMD))}__ 급식"
                )

            self.embed.add_field(
                name=f"{self.add_emoji(result.MMEAL_SC_NM)} ({result.CAL_INFO})",
                value=f"{self.parse_br_tag(result.DDISH_NM)}",
                inline=True,
            )

        return self.embed
