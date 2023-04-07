from typing import Any, Literal, Optional, overload

from crenata.discord import CrenataInteraction
from crenata.discord.embed import school_result_embed_maker
from crenata.discord.paginator import Paginator
from crenata.entities import Preferences
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
    view = Paginator(interaction.user.id, results, school_result_embed_maker)

    await interaction.response.send_message(
        embed=view.embeds[0], view=view, ephemeral=ephemeral
    )

    if not await view.wait():
        if view.selected:
            data = view.data[view.index]
            return data

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
) -> tuple[str, str, str, Preferences]:
    ...


@overload
async def school_info(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    *,
    handle_detail: Literal[True],
) -> tuple[str, str, str, int, int, Preferences]:
    ...


@overload
async def school_info(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    handle_detail: bool = False,
) -> tuple[str, str, str, int, int, Preferences] | tuple[str, str, str, Preferences]:
    ...


async def school_info(
    interaction: CrenataInteraction,
    school_name: Optional[str] = None,
    grade: Optional[int] = None,
    room: Optional[int] = None,
    handle_detail: bool = False,
) -> tuple[str, str, str, int, int, Preferences] | tuple[str, str, str, Preferences]:
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

        preferences = Preferences(private=False)
    else:
        user = await interaction.client.ctx.query.user.read(interaction.user.id)

        if not user or not user.school_info:
            raise NeedSchoolName

        school_name = user.school_info.school_name
        edu_office_code = user.school_info.ATPT_OFCDC_SC_CODE
        standard_school_code = user.school_info.SD_SCHUL_CODE
        preferences = user.preferences.to_entity()

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
