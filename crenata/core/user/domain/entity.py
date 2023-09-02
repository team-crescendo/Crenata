from dataclasses import dataclass
from typing import Optional

from crenata.core.preferences.domain.entity import Preferences
from crenata.core.schoolinfo.domain.entity import SchoolInfo


@dataclass
class User:
    discord_id: int
    preferences: Preferences
    school_info: Optional[SchoolInfo]

    @classmethod
    def default(cls, discord_id: int):
        return cls(
            discord_id=discord_id,
            preferences=Preferences.default(),
            school_info=None,
        )
