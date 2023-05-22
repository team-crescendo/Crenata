from typing import Any, Optional
from discord import Embed
from crenata.abc.builder import AbstractEmbedBuilder
from crenata.utils.datetime import datetime_to_readable, to_datetime


class SchoolResultEmbedBuilder(AbstractEmbedBuilder):
    def build(self, data: Any) -> Embed:
        self.embed.title = data.SCHUL_NM

        self.embed.description = f"🏫 **주소 (도로명)**\n{data.ORG_RDNMA}"
        if data.ENG_SCHUL_NM:
            self.embed.description = f"{data.ENG_SCHUL_NM}\n\n" + self.embed.description

        return self.embed


class DetailSchoolResultEmbedBuilder(SchoolResultEmbedBuilder):
    def add_paragraph(self, string: str) -> str:
        return string + "\n\n--------------------"

    def parse_homepage_url(self, url: str) -> Optional[str]:
        """
        학교 홈페이지 주소를 파싱해주는 함수입니다.
        주소가 없다면 None을 반환합니다.
        """
        if url and url != "http://" and url != "https://":
            if url.startswith("http") or url.startswith("https"):
                return url

            return f"http://{url}"

        return None

    def build(self, data: Any) -> Embed:
        super().build(data)

        if data.ENG_SCHUL_NM:
            self.embed.description = self.add_paragraph(data.ENG_SCHUL_NM)
        else:
            self.embed.description = "--------------------"

        self.embed.set_author(name="🔍 학교 상세 정보")

        kind = f"> {data.SCHUL_KND_SC_NM}"
        if data.SCHUL_KND_SC_NM == "고등학교":
            kind += f"\n> {data.HS_GNRL_BUSNS_SC_NM} {data.HS_SC_NM}"

        if (coedu := data.COEDU_SC_NM) == "남" or coedu == "여":
            coedu += "학교"
        else:
            coedu = "남녀공학"
        kind += f"\n> {coedu}"

        self.embed.add_field(name="❓ 학교 분류", value=self.add_paragraph(kind))
        self.embed.add_field(
            name="⚒️ 설립일", value=datetime_to_readable(to_datetime(data.FOND_YMD))
        )
        self.embed.add_field(
            name="🏫 주소 (도로명)", value=data.ORG_RDNMA, inline=False
        )
        self.embed.add_field(name="📮 우편번호", value=data.ORG_RDNZC)
        self.embed.add_field(name="📲 대표 전화", value=data.ORG_TELNO)
        self.embed.add_field(name="📲 팩스 번호", value=data.ORG_FAXNO)

        if url := self.parse_homepage_url(data.HMPG_ADRES):
            self.embed.add_field(
                name="🔗 학교 홈페이지",
                value=f"[바로가기]({url})",
                inline=False,
            )

        self.embed.set_footer(
            text=(
                "⌛ 마지막 데이터 수정 일자:"
                f" {datetime_to_readable(to_datetime(data.LOAD_DTM))}"
            )
        )

        return self.embed
