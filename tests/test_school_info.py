import pytest

from crenata.database.query import Query
from crenata.database.schema import SchoolInfoSchema


@pytest.mark.asyncio
async def test_school_info_read(query: Query):
    school_info = await query.school_info.read(1)
    assert school_info


@pytest.mark.asyncio
async def test_school_info_update(query: Query, new_school_info: SchoolInfoSchema):
    new_school_info.school_name = "test_school2"
    await query.school_info.update(new_school_info)
    school_info = await query.school_info.read(1)
    assert school_info
    assert school_info.school_name == "test_school2"


@pytest.mark.asyncio
async def test_school_info_delete(query: Query, new_school_info: SchoolInfoSchema):
    await query.school_info.create(new_school_info)
    await query.school_info.delete(new_school_info)
    school_info = await query.school_info.read(1)
    assert school_info is None
