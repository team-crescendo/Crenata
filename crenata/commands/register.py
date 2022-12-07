from discord import app_commands

from crenata.commands.default.register import Register
from crenata.typing import CrenataInteraction
from crenata.utils import defer, use_crenata_command


@app_commands.command(name="등록", description="학교를 등록합니다.")
@app_commands.describe(school_name="등록할 학교 이름입니다.")
@use_crenata_command(Register)
@defer
async def register(
    interaction: CrenataInteraction, school_name: str, grade: int, class_num: int
) -> None:
    ...
    await interaction.execute(school_name, grade, class_num)
