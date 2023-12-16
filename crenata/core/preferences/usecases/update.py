from crenata.core.preferences.domain.entity import Preferences
from crenata.core.preferences.domain.repository import PreferencesRepository


class UpdatePreferencesUseCase:
    def __init__(self, preferences_repository: PreferencesRepository) -> None:
        self.preferences_repository = preferences_repository

    async def execute(self, user_id: int, preferences: Preferences) -> None:
        await self.preferences_repository.update_preferences(user_id, preferences)
