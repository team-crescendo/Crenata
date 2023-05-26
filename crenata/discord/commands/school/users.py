from crenata.discord import CrenataInteraction
from crenata.discord.commands.school import school
from crenata.discord.embed.users import school_users_embed_builder
from crenata.exception import NeedSchoolRegister


@school.command(name="유저", description="나와 학교가 같은 유저 수를 가져옵니다.")
async def users(interaction: CrenataInteraction) -> None:
    user = await interaction.client.ctx.query.user.read(interaction.user.id)

    if not user or not user.school_info:
        raise NeedSchoolRegister

    users = await interaction.client.ctx.query.user.read_all_user_from_school_info(
        user.school_info
    )

    embed = school_users_embed_builder(
        user.school_info.school_name, len(users), user.preferences.private
    )

    await interaction.response.send_message(
        embed=embed, ephemeral=user.preferences.ephemeral
    )
