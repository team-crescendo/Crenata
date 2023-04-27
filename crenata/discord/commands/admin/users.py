from crenata.discord import CrenataInteraction
from crenata.discord.commands.admin import admin
from discord import Embed


@admin.command(name="유저", description="전체 유저 수를 확인합니다.")
async def users(interaction: CrenataInteraction) -> None:
    users = await interaction.client.ctx.query.user.read_all()

    embed = Embed(
        title="유저 수", description=f"현재 {len(users)}명의 유저가 봇을 사용하고 있어요.", color=5681003
    )

    if len(users) < 10:
        embed.add_field(
            name="유저 목록",
            value=" ".join([f"<@{user.id}>" for user in users]),
        )

        return await interaction.response.send_message(
            embed=embed,
        )

    embed.add_field(
        name="유저 목록",
        value=(
            f"{' '.join([f'<@{user.id}>' for user in users[:9]])} and "
            f"{len(users) - 10} more"
        ),
    )

    await interaction.response.send_message(
        embed=embed,
    )
