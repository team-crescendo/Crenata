from re import compile
from typing import Any, Optional

from discord import SelectOption
from discord.ui import Select


def allergy_select(results: Optional[list[Any]]) -> Optional[Select]:
    """
    급식 데이터에서가 알러지 목록을 보여주는 select menu를 만듭니다.
    """
    if not results:
        return None
    allergy_code = [
        "난류",
        "우유",
        "메밀",
        "땅콩",
        "대두",
        "밀",
        "고등어",
        "게",
        "새우",
        "돼지고기",
        "복숭아",
        "토마토",
        "아황산류",
        "호두",
        "닭고기",
        "쇠고기",
        "오징어",
        "조개류",
        "잣",
    ]
    result = []
    for data in results:
        string = data.DDISH_NM
        allergy_re = compile(r"\([\d{1,2}.]+\)")
        meals = string.split("<br/>")
        for meal in meals:
            meal_allergy = [allergy_re.split(meal)[0][:-2]]
            code = allergy_re.findall(meal)
            if code:
                code = code[0][1:-1]
                codes = code.split(".")[:-1]
                for allergy in codes:
                    meal_allergy.append(allergy_code[int(allergy) - 1])
            else:
                meal_allergy.append("없음")
            if meal_allergy not in result:
                result.append(meal_allergy)
    select_options = []
    for meal in result:
        select_options.append(
            SelectOption(label=meal[0], description=", ".join(meal[1:]))
        )
    allergy_select_menu = Select(placeholder="알레르기 정보", options=select_options)
    return allergy_select_menu
