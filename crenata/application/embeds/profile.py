from discord import Member, User

from crenata.application.embeds import CrenataEmbed
from crenata.application.utils import follow_private_preference


def profile_embed_builder(
    user: User | Member,
    school_name: str,
    school_grade: str,
    school_room: str,
    private: bool,
    ephemeral: bool,
) -> CrenataEmbed:
    embed = CrenataEmbed(title=user.name)

    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_author(name="프로필")

    grade_room = f"{school_grade}학년 {school_room}반"

    (
        school_name,
        grade_room,
    ) = follow_private_preference(
        is_private=private, school_name=school_name, grade_room=grade_room
    ).values()

    embed.add_field(
        name="🏫 내 학교 정보",
        value=(
            f"**[학교]** {school_name}\n**[학년/반]** {grade_room}\n\n"
            "> `/학교 설정`으로 학교 정보 변경이 가능합니다.\n\n"
            "-----"
        ),
        inline=False,
    )

    embed.add_field(
        name="🔒 공개 여부 설정",
        value=(
            f"**[내 학교 공개하기]** {'❌ 비공개' if private else '⭕ 공개'}\n"
            f"**[명령어 답변 공개하기]** {'❌ 비공개' if ephemeral else '⭕ 공개'}\n\n"
            "> `/환경설정 변경`으로 환경설정 변경이 가능합니다.\n\n"
            "-----"
        ),
        inline=False,
    )

    return embed
