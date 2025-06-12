from typing import Optional

from crenata.application.embeds import CrenataEmbed
from crenata.core.school.domain.entity import School
from crenata.infrastructure.utils.datetime import datetime_to_readable


def school_embed_builder(school: School) -> CrenataEmbed:
    embed = CrenataEmbed(title=school.name)

    embed.description = f"🏫 **주소 (도로명)**\n{school.street_name_address}"

    if school.english_name:
        embed.description = f"{school.english_name}\n\n" + embed.description

    return embed


def _add_paragraph(string: str) -> str:
    return string + "\n\n--------------------"


def _parse_homepage_url(url: str) -> Optional[str]:
    """
    학교 홈페이지 주소를 파싱해 주는 함수입니다.
    주소가 없다면 None을 반환합니다.
    """
    if url and url != "http://" and url != "https://":
        if url.startswith("http") or url.startswith("https"):
            return url

        return f"http://{url}"


def _handle_english_school_name(school_name: Optional[str]) -> str:
    if school_name:
        return _add_paragraph(school_name)

    return "--------------------"


def _handle_coeducation(school: School) -> str:
    if school.coeducation == "남" or school.coeducation == "여":
        return school.coeducation + "학교"

    else:
        return "남녀공학"


def _handle_school_type(school: School) -> str:
    kind = f"> {school.kind}"

    if school.kind == "고등학교":
        kind += (
            f"\n> {school.highschool_general_or_business} {school.highschool_category}"
        )

    kind += f"\n> { _handle_coeducation(school)}"

    return kind


def detail_school_school_embed_builder(school: School) -> CrenataEmbed:
    embed = CrenataEmbed()

    embed.description = _handle_english_school_name(school.english_name)
    embed.set_author(name="🔍 학교 상세 정보")

    kind = _handle_school_type(school)

    embed.add_field(name="❓ 학교 분류", value=_add_paragraph(kind))
    embed.add_field(name="⚒️ 설립일", value=datetime_to_readable(school.founding_date))
    embed.add_field(
        name="🏫 주소 (도로명)", value=school.street_name_address, inline=False
    )
    embed.add_field(name="📮 우편번호", value=school.zip_code)
    embed.add_field(name="📲 대표 전화", value=school.telephone_number)
    embed.add_field(name="📲 팩스 번호", value=school.fax_number)

    if url := _parse_homepage_url(school.homepage_address):
        embed.add_field(
            name="🔗 학교 홈페이지",
            value=f"[바로가기]({url})",
            inline=False,
        )

    return embed
