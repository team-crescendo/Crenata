from datetime import datetime
from io import BytesIO
from typing import Any, Literal, Optional

from crenata.discord.timetable import make_timetable_image
from crenata.utils.datetime import datetime_to_readable, to_datetime
from discord import Embed


def add_paragraph(string: str) -> str:
    return string + "\n\n--------------------"


def add_end_paragraph(string: str) -> str:
    return "--------------------\n\n" + string


def add_emoji(string: Literal["조식", "중식", "석식"]) -> str:
    """
    조식, 중식, 석식에 맞는 이모지를 추가해주는 함수입니다.
    """
    emoji = {"조식": "⛅", "중식": "☀️", "석식": "🌙"}
    return f"{emoji.get(string, None)} {string}"


def parse_br_tag(string: str) -> str:
    """
    <br/> 태그를 개행문자로 바꿔주는 함수입니다.
    """
    return "\n".join([f"> {word}" for word in string.split("<br/>")])


def school_result_embed_maker(
    result: Any, index: Optional[int] = 1, total: Optional[int] = 1
) -> Embed:
    """
    학교 검색 결과를 Embed로 만들어주는 함수입니다.
    """

    embed = Embed(
        title=result.SCHUL_NM,
        color=5681003,
    )

    if result.ENG_SCHUL_NM:
        embed.description = add_paragraph(result.ENG_SCHUL_NM)

    embed.set_author(name="🔍 학교 검색 결과")
    embed.add_field(name="❓ 학교 분류", value=result.SCHUL_KND_SC_NM)
    embed.add_field(
        name="⚒️ 설립일", value=datetime_to_readable(to_datetime(result.FOND_YMD))
    )
    embed.add_field(name="🏫 주소 (도로명)", value=result.ORG_RDNMA, inline=False)
    embed.add_field(name="📮 우편번호", value=result.ORG_RDNZC)
    embed.add_field(name="📲 대표 전화", value=result.ORG_TELNO)
    if (
        result.HMPG_ADRES
        and result.HMPG_ADRES != "http://"
        or result.HMPG_ADRES != "https://"
    ):
        embed.add_field(
            name="🔗 학교 홈페이지",
            value=f"[바로가기]({parse_hompage_url(result.HMPG_ADRES)})",
            inline=False,
        )
    embed.set_footer(text=f"{index}/{total}")
    return embed


def detailed_school_result_embed_maker(result: Any) -> Embed:
    """
    학교 검색 결과를 Embed로 만들어주는 함수입니다.
    학교 1개만 자세하게 표시할 때 사용합니다.
    """
    embed = school_result_embed_maker(result)
    embed.set_author(name="🔍 학교 상세 정보")
    if (coedu := result.COEDU_SC_NM) == "남" or coedu == "여":
        coedu += "학교"
    else:
        coedu = "남녀공학"
    embed.add_field(name="⚥ 남녀공학", value=coedu)
    embed.add_field(name="📲 팩스 번호", value=result.ORG_FAXNO)
    embed.set_footer(
        text=f"⌛ 마지막 데이터 수정 일자: {datetime_to_readable(to_datetime(result.LOAD_DTM))}"
    )
    return embed


def meal_page(results: Optional[list[Any]], private: bool) -> Optional[Embed]:
    """
    급식 검색 결과를 Embed로 만들어주는 함수입니다.
    """
    if not results:
        return None

    r = results[0]
    school_name = r.SCHUL_NM
    if private:
        school_name = "비공개"

    embed = Embed(
        title=f'"{school_name}" 의 급식 정보',
        description=f"__{datetime_to_readable(to_datetime(r.MLSV_FROM_YMD))}__ 급식",
        color=5681003,
    )
    embed.set_author(name="🔍 급식 검색 결과")

    for result in results:
        embed.add_field(
            name=f"{add_emoji(result.MMEAL_SC_NM)}",
            value=f"{parse_br_tag(result.DDISH_NM)}",
            inline=True,
        )

    return embed


async def time_table_embed_maker(
    results: list[list[Any]], date: datetime, private: bool
) -> tuple[Embed, BytesIO]:
    """
    시간표 검색 결과를 Embed로 만들어주는 함수입니다.
    """
    r = results[0][0]
    school_name = r.SCHUL_NM
    if private:
        school_name = "비공개"
    image = await make_timetable_image(results, date)
    embed = Embed(
        title=f"🗓️ 시간표",
        color=5681003,
        description=f"{school_name} __{datetime_to_readable(date)}__ 시간표",
    )
    embed.set_image(url="attachment://timetable.png")

    return embed, image


def parse_hompage_url(url: str) -> str:
    """
    학교 홈페이지 주소를 파싱해주는 함수입니다.
    """
    if url.startswith("http") or url.startswith("https"):
        return url
    else:
        return f"http://{url}"
