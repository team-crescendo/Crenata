import pytest

from crenata.database.query import Query
from crenata.database.schema import PreferencesSchema


@pytest.mark.asyncio
async def test_preferences_read(query: Query):
    preferences = await query.preferences.read(1)
    assert preferences


@pytest.mark.asyncio
async def test_preferences_update(query: Query, new_preferences: PreferencesSchema):
    new_preferences.private = False
    await query.preferences.update(new_preferences)
    preferences = await query.preferences.read(1)
    assert preferences
    assert preferences.private is False


@pytest.mark.asyncio
async def test_preferences_delete(query: Query, new_preferences: PreferencesSchema):
    await query.preferences.delete(new_preferences)
    preferences = await query.preferences.read(1)
    assert preferences is None
