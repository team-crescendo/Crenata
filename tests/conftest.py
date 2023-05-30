import asyncio

import pytest

from crenata.database.base import Base
from crenata.database.query import Query
from crenata.database.schema import *
from crenata.neispy import CrenataNeispy


@pytest.fixture
def new_preferences():
    return PreferencesSchema(user_id=1)


@pytest.fixture
def new_school_info():
    return SchoolInfoSchema(
        user_id=1,
        school_name="test_school",
        grade=1,
        room=1,
        ATPT_OFCDC_SC_CODE="test_code",
        SD_SCHUL_CODE="test_code",
    )


@pytest.fixture
def new_user(new_preferences: PreferencesSchema, new_school_info: SchoolInfoSchema):
    return UserSchema(id=1, preferences=new_preferences, school_info=new_school_info)


@pytest.fixture
def neispy():
    return CrenataNeispy.create("")


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
@pytest.mark.asyncio
async def _query():
    # if you want to use sqlite in memory, use this line instead of the next one
    # query = await Query.setup("sqlite+aiosqlite:///:memory:")
    query = await Query.setup("postgresql+asyncpg://postgres:test@localhost/rena")
    return query


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def query(_query: Query, new_user: UserSchema):
    async with _query.database.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all, checkfirst=True)
    await _query.user.create(new_user)
    yield _query
    async with _query.database.engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
