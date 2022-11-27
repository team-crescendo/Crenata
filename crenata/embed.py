from typing import Any

from discord import Embed


def add_paragraph(string: str) -> str:
    return string + "\n\n--------------------"


def add_end_paragraph(string: str) -> str:
    return "--------------------\n\n" + string


def school_result_embed_maker(result: Any, index: int, total: int) -> Embed:
    """
    학교 검색 결과를 Embed로 만들어주는 함수입니다.
    """
    embed = Embed(
        title=result.SCHUL_NM,
        description=add_paragraph(result.ENG_SCHUL_NM),
        color=5681003,
    )
    embed.set_author(name="🔍 학교 검색 결과")
    embed.add_field(name="❓ 학교 분류", value=add_paragraph(result.SCHUL_KND_SC_NM))
    embed.add_field(name="⚒️ 설립일", value=result.FOND_YMD)
    embed.add_field(name="🏫 주소 (도로명)", value=result.ORG_RDNMA, inline=False)
    embed.add_field(name="📮 우편번호", value=result.ORG_RDNZC)
    embed.add_field(name="📲 대표 전화", value=result.ORG_TELNO)
    embed.add_field(
        name="기타",
        value=f"[🔗 학교 홈페이지 바로가기]({result.HMPG_ADRES})",
        inline=False,
    )
    embed.set_footer(text=f"{index}/{total}")
    return embed


def meal_result_embed_maker(result: Any, index: int, total: int) -> Embed:
    """
    급식 검색 결과를 Embed로 만들어주는 함수입니다.
    """
    embed = Embed(title="검색된 정보 입니다.", description=result.SCHUL_NM)
    return embed
