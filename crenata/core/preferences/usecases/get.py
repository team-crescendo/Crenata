from crenata.core.preferences.domain.entity import Preferences
from crenata.core.preferences.domain.repository import PreferencesRepository
from crenata.core.preferences.exceptions import PreferencesNotFound


class GetPreferencesUseCase:
    def __init__(self, preferences_repository: PreferencesRepository) -> None:
        self.preferences_repository = preferences_repository

    async def execute(self, user_id: int) -> Preferences:
        nullable_prefernces = await self.preferences_repository.get_preferences(user_id)

        if nullable_prefernces is None:
            raise PreferencesNotFound

        return nullable_prefernces
