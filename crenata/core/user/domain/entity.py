from dataclasses import dataclass

from crenata.core.preferences.domain.entity import Preferences
from crenata.core.schoolinfo.domain.entity import SchoolInfo


@dataclass
class User:
    preferences: Preferences
    school_info: SchoolInfo
