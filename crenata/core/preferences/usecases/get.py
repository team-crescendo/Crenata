from crenata.core.preferences.domain.entity import Preferences
from crenata.core.preferences.domain.repository import PreferencesRepository
from crenata.core.user.exceptions import UserNotFound


class GetPreferencesUseCase:
    def __init__(self, preferences_repository: PreferencesRepository) -> None:
        self.preferences_repository = preferences_repository

    async def execute(self, user_id: int) -> Preferences:
        preferences = await self.preferences_repository.get_preferences(user_id)

        if preferences is None:
            raise UserNotFound

        return preferences
