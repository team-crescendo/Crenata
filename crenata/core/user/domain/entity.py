from dataclasses import dataclass
from typing import Optional

from crenata.core.preferences.domain.entity import Preferences
from crenata.core.schoolinfo.domain.entity import SchoolInfo


@dataclass
class User:
    discord_id: int
    preferences: Preferences
    school_info: Optional[SchoolInfo]
