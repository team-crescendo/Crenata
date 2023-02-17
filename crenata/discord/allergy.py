from re import compile
from typing import Any, Final, Optional

from discord import SelectOption

ALLERGY_CODES: Final = {
    "1": "난류",
    "2": "우유",
    "3": "메밀",
    "4": "땅콩",
    "5": "대두",
    "6": "밀",
    "7": "고등어",
    "8": "게",
    "9": "새우",
    "10": "돼지고기",
    "11": "복숭아",
    "12": "토마토",
    "13": "아황산류",
    "14": "호두",
    "15": "닭고기",
    "16": "쇠고기",
    "17": "오징어",
    "18": "조개류",
    "19": "잣",
}


def allergy_select_option(results: Optional[list[Any]]) -> Optional[list[SelectOption]]:
    if not results:
        return None
    select_options: list[SelectOption] = []  # 리턴할 옵션
    meals: list[str] = []  # 표시되는 메뉴들
    allergy_menus = 0  # 알레르기 정보가 있는 메뉴 수
    allergy_re = compile(
        r"\(?[\d{1,2}.]+\.\)?"
    )  # 정규식, 시작과 끝에 () 있을수도, "'1~2자리 숫자'." 반복, 끝날때 .
    for data in results:
        for meal in data.DDISH_NM.split("<br/>"):  # 메뉴별로 split
            meal_result = []  # 이 메뉴의 정보
            meal_name = allergy_re.sub("", meal)  # 알러지 부분을 제외한 부분을 메뉴 이름으로
            if not (allergies := allergy_re.findall(meal)):  # 알러지없음
                meal_result.append("없음")
            else:
                allergy_menus += 1
                allergies_split = (
                    allergies[0]
                    .replace("(", "")
                    .replace(")", "")
                    .split(".")[:-1]  # 괄호없애고 .로 나눠서 숫자 분리, 마지막 '' 없애기
                )
                for allergy in allergies_split:
                    meal_result.append(ALLERGY_CODES[allergy])  # 숫자 -> 이름
            if meal_name not in meals:  # 중복메뉴 없음
                meals.append(meal_name)
                select_options.append(
                    SelectOption(
                        label=meal_name,
                        description=", ".join(meal_result),  # ', '로 구분해서 합치기
                    )
                )
    if not allergy_menus:
        return None
    return select_options
