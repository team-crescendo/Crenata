from typing import Any, Optional

from crenata.utils.datetime import datetime_to_readable, to_datetime
from crenata.utils.discord import CrenataEmbed


def school_result_embed_builder(result: Any) -> CrenataEmbed:
    embed = CrenataEmbed()
    embed.title = result.SCHUL_NM

    embed.description = f"🏫 **주소 (도로명)**\n{result.ORG_RDNMA}"
    if result.ENG_SCHUL_NM:
        embed.description = f"{result.ENG_SCHUL_NM}\n\n" + embed.description

    return embed


def _add_paragraph(string: str) -> str:
    return string + "\n\n--------------------"


def _parse_homepage_url(url: str) -> Optional[str]:
    """
    학교 홈페이지 주소를 파싱해주는 함수입니다.
    주소가 없다면 None을 반환합니다.
    """
    if url and url != "http://" and url != "https://":
        if url.startswith("http") or url.startswith("https"):
            return url

        return f"http://{url}"

    return None


def _handle_english_school_name(school_name: Optional[str]) -> str:
    if school_name:
        return _add_paragraph(school_name)
    return "--------------------"


def _handle_coeducation(result: Any) -> str:
    coedu_school_name: str = result.COEDU_SC_NM
    if coedu_school_name == "남" or coedu_school_name == "여":
        coedu_school_name += "학교"
    else:
        coedu_school_name = "남녀공학"
    return coedu_school_name


def _handle_school_type(result: Any) -> str:
    kind = f"> {result.SCHUL_KND_SC_NM}"
    if result.SCHUL_KND_SC_NM == "고등학교":
        kind += f"\n> {result.HS_GNRL_BUSNS_SC_NM} {result.HS_SC_NM}"
    kind += f"\n> { _handle_coeducation(result)}"
    return kind


def detail_school_result_embed_builder(result: Any) -> CrenataEmbed:
    embed = CrenataEmbed()
    kind = _handle_school_type(result)
    embed.description = _handle_english_school_name(result.ENG_SCHUL_NM)
    embed.set_author(name="🔍 학교 상세 정보")
    embed.add_field(name="❓ 학교 분류", value=_add_paragraph(kind))
    embed.add_field(
        name="⚒️ 설립일",
        value=datetime_to_readable(to_datetime(result.FOND_YMD)),
    )
    embed.add_field(name="🏫 주소 (도로명)", value=result.ORG_RDNMA, inline=False)
    embed.add_field(name="📮 우편번호", value=result.ORG_RDNZC)
    embed.add_field(name="📲 대표 전화", value=result.ORG_TELNO)
    embed.add_field(name="📲 팩스 번호", value=result.ORG_FAXNO)

    if url := _parse_homepage_url(result.HMPG_ADRES):
        embed.add_field(
            name="🔗 학교 홈페이지",
            value=f"[바로가기]({url})",
            inline=False,
        )

    embed.set_footer(
        text=f"⌛ 마지막 데이터 수정 일자: {datetime_to_readable(to_datetime(result.LOAD_DTM))}"
    )

    return embed
