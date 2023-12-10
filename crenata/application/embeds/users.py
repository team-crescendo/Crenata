from crenata.application.embeds import CrenataEmbed
from crenata.application.utils import follow_private_preference


def school_users_embed_builder(
    school_name: str, users: int, is_private: bool
) -> CrenataEmbed:
    embed = CrenataEmbed()
    (school_name,) = follow_private_preference(is_private, school_name=school_name)
    embed.title = f'"{school_name}" 의 유저 수'
    embed.description = f"👥 {users} 명"
    embed.set_author(name="🔍 학교 사용자 검색 결과")
    return embed
