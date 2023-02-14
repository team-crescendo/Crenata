import pytest

from crenata.database.query import Query
from crenata.database.schema import UserSchema


@pytest.mark.asyncio
async def test_user_read(query: Query):
    user = await query.user.read(1)
    assert user


@pytest.mark.asyncio
async def test_user_update(query: Query, new_user: UserSchema):
    new_user.preferences.private = False
    await query.user.update(new_user)
    user = await query.user.read(1)
    assert user
    assert user.preferences.private is False


@pytest.mark.asyncio
async def test_user_delete(query: Query, new_user: UserSchema):
    await query.user.delete(new_user)
    user = await query.user.read(1)
    assert user is None
