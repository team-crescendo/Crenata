from typing import Any, Literal, Optional, overload

from crenata.database.schema.preferences import PreferencesSchema
from crenata.discord import CrenataInteraction
from crenata.discord.embed.school import school_result_embed_builder
from crenata.discord.paginator import Paginator
from crenata.exception import (
    MustBeGreaterThanOne,
    NeedGradeAndRoom,
    NeedSchoolName,
    UserCanceled,
    ViewTimeout,
)


async def school_page(
    interaction: CrenataInteraction, school_name: str, *, ephemeral: bool = False
) -> Any:
    """
    학교를 검색하고 선택할수있는 페이지를 보여줍니다.
    """

    results = await interaction.client.ctx.neispy.search_school(school_name)
    embeds = [school_result_embed_builder(result) for result in results]
    view = Paginator(interaction.user.id, embeds)

    await interaction.response.send_message(
        embed=view.embeds[0], view=view, ephemeral=ephemeral
    )

    if not await view.wait():
        if view.selected:
            return results[view.index]

        raise UserCanceled

    raise ViewTimeout


# https://github.com/python/mypy/issues/4020#issuecomment-748289714
@overload
async def school_info(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    *,
    handle_detail: Literal[False] = False,
) -> tuple[str, str, str, PreferencesSchema]:
    ...


@overload
async def school_info(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    *,
    handle_detail: Literal[True],
) -> tuple[str, str, str, int, int, PreferencesSchema]:
    ...


@overload
async def school_info(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    handle_detail: bool = False,
) -> (
    tuple[str, str, str, int, int, PreferencesSchema]
    | tuple[str, str, str, PreferencesSchema]
):
    ...


async def school_info(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    handle_detail: bool = False,
) -> (
    tuple[str, str, str, int, int, PreferencesSchema]
    | tuple[str, str, str, PreferencesSchema]
):
    """
    데이터베이스에 저장된 학교 정보를 가져오거나, 학교 이름을 입력받아 학교 정보를 가져옵니다.
    """
    # TODO: 학교 정보 엔티티로 리턴
    if school_name:
        if handle_detail:
            if not grade or not room:
                raise NeedGradeAndRoom

            if grade < 1 or room < 1:
                raise MustBeGreaterThanOne

        results = await school_page(interaction, school_name)
        edu_office_code = str(results.ATPT_OFCDC_SC_CODE)
        standard_school_code = str(results.SD_SCHUL_CODE)
        school_name = str(results.SCHUL_NM)

        preferences = PreferencesSchema()
    else:
        user = await interaction.client.ctx.query.user.read(interaction.user.id)

        if not user or not user.school_info:
            raise NeedSchoolName

        school_name = user.school_info.school_name
        edu_office_code = user.school_info.ATPT_OFCDC_SC_CODE
        standard_school_code = user.school_info.SD_SCHUL_CODE
        preferences = user.preferences

        await interaction.response.send_message(
            "정보를 가져오는중 입니다.", ephemeral=preferences.ephemeral
        )

        if not grade:
            grade = user.school_info.grade
        if not room:
            room = user.school_info.room

    school_code = (edu_office_code, standard_school_code)

    if handle_detail and grade and room:
        return school_name, *school_code, grade, room, preferences

    return school_name, *school_code, preferences
