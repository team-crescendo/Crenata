from abc import ABC, abstractmethod
from typing import Optional

from crenata.core.preferences.domain.entity import Preferences


class PreferencesRepository(ABC):
    @abstractmethod
    async def get_preferences(self, user_id: int) -> Optional[Preferences]: ...

    @abstractmethod
    async def update_preferences(
        self, user_id: int, preferences: Preferences
    ) -> None: ...
