from crenata.commands.register import Register
from crenata.discord import CrenataInteraction
from discord import app_commands


@app_commands.command(name="등록", description="학교를 등록합니다.")
@app_commands.describe(school_name="등록할 학교 이름입니다.")
async def register(
    interaction: CrenataInteraction, school_name: str, grade: int, class_num: int
) -> None:
    command = interaction.client.get_command(Register, interaction)
    await command.execute(school_name, grade, class_num)
