from datetime import datetime
from typing import Any, Optional

import pytest

from crenata.utils.datetime import (
    datetime_to_readable,
    to_datetime,
    to_weekday,
    to_yyyymmdd,
    use_current_date,
)
from neispy.utils import KST


def test_to_datetime():
    assert to_datetime("20210101") == datetime(2021, 1, 1)


def test_to_yyyymmdd():
    assert to_yyyymmdd(datetime(2021, 1, 1)) == "20210101"


def test_datetime_to_readable():
    assert datetime_to_readable(datetime(2021, 1, 1)) == "2021년 01월 01일"


def test_to_weekday():
    assert to_weekday(datetime(2021, 1, 1)) == "금"


@pytest.mark.asyncio
async def test_use_current_date():
    @use_current_date
    async def inner_test(**kwargs: Any):
        now = datetime.now(KST)
        decorated_now: Optional[datetime] = kwargs.get("date")
        assert decorated_now
        assert now.year == decorated_now.year
        assert now.month == decorated_now.month
        assert now.day == decorated_now.day
        assert now.hour == decorated_now.hour
        assert now.minute == decorated_now.minute

    await inner_test()
