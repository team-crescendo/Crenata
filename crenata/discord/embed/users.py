from typing import Any

from crenata.abc.builder import AbstractEmbedBuilder
from discord import Embed


class SchoolUsersEmbedBuilder(AbstractEmbedBuilder):
    def build(self, *data: Any) -> Embed:
        school_name, users = data
        school_name = self.follow_private_preference(school_name)
        self.embed.title = f'"{school_name}" 의 유저 수'
        self.embed.description = f"👥 {users} 명"
        self.embed.set_author(name="🔍 학교 사용자 검색 결과")
        return self.embed
