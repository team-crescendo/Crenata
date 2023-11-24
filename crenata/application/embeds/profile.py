from crenata.application.embeds import CrenataEmbed
from crenata.application.utils import follow_private_preference


def profile_embed_builder(
    user_name: str,
    school_name: str,
    school_grade: str,
    school_room: str,
    private: bool,
    ephemeral: bool,
) -> CrenataEmbed:
    embed = CrenataEmbed()

    embed.title = "프로필"
    embed.add_field(name=user_name, value="", inline=False)

    if school_name != "":
        grade_room = school_grade + "학년 " + school_room + "반"

        (
            school_name,
            grade_room,
        ) = follow_private_preference(
            is_private=private, school_name=school_name, grade_room=grade_room
        ).values()

        embed.add_field(
            name="🏫 내 학교 정보",
            value="**[학교]** " + school_name + "\n**[학년/반]** " + grade_room + "\n",
            inline=False,
        )
        embed.add_field(
            name="", value="> `/학교 설정`으로 학교 정보 변경이 가능합니다." + "\n", inline=False
        )
        embed.add_field(name="", value="-----", inline=False)

    if private:
        txt_private = "❌ 비공개"
    else:
        txt_private = "⭕ 공개"

    if ephemeral:
        txt_ephemeral = "❌ 비공개"
    else:
        txt_ephemeral = "⭕ 공개"

    embed.add_field(
        name="🔒 공개 여부 설정",
        value="**[내 학교 공개하기]** "
        + txt_private
        + "\n**[명령어 답변 공개하기]** "
        + txt_ephemeral
        + "\n",
        inline=False,
    )
    embed.add_field(
        name="", value="> `/환경설정 변경`으로 환경설정 변경이 가능합니다." + "\n", inline=False
    )
    embed.add_field(name="", value="-----", inline=False)

    # embed.description = f"{school_name} __{datetime_to_readable(date)}__ 시간표"
    # embed.set_image(url="attachment://timetable.png")

    return embed
