from types import SimpleNamespace

from crenata.discord.embed.meal import meal_embed_builder


def test_meal_embed_builder():
    data = SimpleNamespace()

    data.MLSV_FROM_YMD = "20220303"
    data.MMEAL_SC_NM = "조식"
    data.CAL_INFO = "5000kcal"
    data.DDISH_NM = "밥<br/>반찬<br/>메인<br/>국<br/>김치<br/>디저트"
    data.SCHUL_NM = "학교"

    embed = meal_embed_builder([data], True)

    assert embed.to_dict() == {
        "title": '"비공개" 의 급식 정보',
        "description": "__2022년 03월 03일__ 급식",
        "color": 5681003,
        "author": {"name": "🔍 급식 검색 결과"},
        "fields": [
            {
                "name": "⛅ 조식 (5000kcal)",
                "value": "> 밥\n> 반찬\n> 메인\n> 국\n> 김치\n> 디저트",
                "inline": True,
            },
        ],
        "type": "rich",
    }
