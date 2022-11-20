from typing import Any

from discord import Embed


def school_result_embed_maker(result: Any, index: int, total: int) -> Embed:
    """
    학교 검색 결과를 Embed로 만들어주는 함수입니다.
    """
    embed = Embed(title="검색된 정보 입니다.", description=result.SCHUL_NM)
    embed.add_field(name="주소", value=result.ORG_RDNMA)
    embed.add_field(name="우편번호", value=result.ORG_RDNZC)
    embed.set_footer(text=f"{index}/{total}")
    return embed


def meal_result_embed_maker(result: Any, index: int, total: int) -> Embed:
    """
    급식 검색 결과를 Embed로 만들어주는 함수입니다.
    """
    embed = Embed(title="검색된 정보 입니다.", description=result.SCHUL_NM)
    return embed