import pytest

from crenata.neispy import CrenataNeispy
from crenata.utils.datetime import to_datetime
from neispy.error import DataNotFound


@pytest.mark.asyncio
async def test_search_school(neispy: CrenataNeispy):
    result = await neispy.search_school("구월중학교")
    assert result


@pytest.mark.asyncio
async def test_search_school_not_found(neispy: CrenataNeispy):
    with pytest.raises(DataNotFound):
        await neispy.search_school("thisistestschoolname")


@pytest.mark.asyncio
async def test_get_meal(neispy: CrenataNeispy):
    result = await neispy.get_meal("E10", "7341068", date=to_datetime("20220525"))
    assert result


@pytest.mark.asyncio
async def test_get_meal_not_found(neispy: CrenataNeispy):
    with pytest.raises(DataNotFound):
        await neispy.get_meal("E10", "7341068", date=to_datetime("20220505"))


@pytest.mark.asyncio
async def test_get_time_table(neispy: CrenataNeispy):
    result = await neispy.get_time_table(
        "E10", "7341068", "구월중학교", 1, 1, date=to_datetime("20220525")
    )
    assert result


@pytest.mark.asyncio
async def test_get_week_time_table(neispy: CrenataNeispy):
    d = to_datetime("20220525")
    results, date = await neispy.get_week_time_table(
        "E10", "7341068", "구월중학교", 1, 1, date=d
    )
    assert results

    assert date == d

    for result in results:
        assert result
