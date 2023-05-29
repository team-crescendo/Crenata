from crenata.database.schema import SchoolInfoSchema
from crenata.discord import CrenataInteraction
from crenata.discord.commands.school import school
from crenata.discord.interaction import school_page
from crenata.exception import MustBeGreaterThanOne
from crenata.utils.discord import InteractionLock
from discord import app_commands


@school.command(name="설정", description="학교를 설정합니다.")  # type: ignore[arg-type]
@app_commands.describe(school_name="설정할 학교 이름입니다.")
@app_commands.describe(grade="설정할 학년입니다.")
@app_commands.describe(room="설정할 반입니다.")
async def school_set(
    interaction: CrenataInteraction, school_name: str, grade: int, room: int
) -> None:
    async with InteractionLock(interaction):
        if grade < 1 or room < 1:
            raise MustBeGreaterThanOne

        user_school_info = await interaction.client.ctx.query.school_info.read(
            interaction.user.id
        )

        data = await school_page(interaction, school_name, ephemeral=True)

        school_info = SchoolInfoSchema(
            user_id=interaction.user.id,
            school_name=data.SCHUL_NM,
            grade=grade,
            room=room,
            ATPT_OFCDC_SC_CODE=data.ATPT_OFCDC_SC_CODE,
            SD_SCHUL_CODE=data.SD_SCHUL_CODE,
        )

        if user_school_info:
            school_info.id = user_school_info.id
            await interaction.client.ctx.query.school_info.update(school_info)
            await interaction.edit_original_response(
                content="성공적으로 수정되었어요.",
                embed=None,
                view=None,
            )
            return

        await interaction.client.ctx.query.school_info.create(school_info)

        await interaction.edit_original_response(
            content="성공적으로 등록되었어요.",
            embed=None,
            view=None,
        )
