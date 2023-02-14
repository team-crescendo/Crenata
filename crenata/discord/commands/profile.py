from crenata.discord import CrenataInteraction
from discord import Embed, app_commands


@app_commands.command(name="프로필", description="내 프로필을 확인합니다.")
async def profile(interaction: CrenataInteraction) -> None:
    user = await interaction.client.ctx.query.user.read(interaction.user.id)

    if not user:
        await interaction.response.send_message(
            content="가입되어있지 않아요. ``/가입`` 을 통해 먼저 가입해주세요.", ephemeral=True
        )
        return

    embed = Embed(
        title=f"{interaction.user.name}",
        color=5681003,
    )

    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.set_author(name="프로필")

    if user.school_info:
        grade = f" {user.school_info.grade}학년 {user.school_info.room}반"
        school = user.school_info.school_name
        if user.preferences.private:
            school = grade = "비공개"

        value = (
            f"**[학교]** {school}\n**[학년/반]** {grade}\n\n"
            "> `/학교 설정` 으로 내 학교 정보를 고칠 수 있어요.\n\n-----"
        )

        embed.add_field(name="🏫 내 학교 정보", value=value)

    value = (
        f"**[ 내 학교 공개하기 ]** {'❌ 비공개' if user.preferences.private else '⭕ 공개'}\n"
        f"**[ 명령어 답변 공개하기 ]** {'❌ 비공개' if user.preferences.ephemeral else '⭕ 공개'}\n\n"
        "> `/환경설정 변경` 으로 환경설정을 고칠 수 있어요.\n\n-----"
    )
    embed.add_field(name="🔒 공개 여부 설정", value=value, inline=False)

    await interaction.response.send_message(
        embed=embed, ephemeral=user.preferences.ephemeral
    )
