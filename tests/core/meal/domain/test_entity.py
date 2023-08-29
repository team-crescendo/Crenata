from datetime import datetime

from crenata.core.meal.domain.entity import Meal


def test_meal():
    meal = Meal(
        name="test",
        dish_name="test",
        school_name="테스트 초등학교",
        calorie="1000kcal",
        date=datetime(2021, 1, 1),
    )

    assert meal.name == "test"
    assert meal.dish_name == "test"
    assert meal.school_name == "테스트 초등학교"
    assert meal.calorie == "1000kcal"
    assert meal.date == datetime(2021, 1, 1)
