from dataclasses import dataclass, field
from typing import Optional

from crenata.abc.domain import AbstractDomain
from crenata.entities.preferences import Preferences
from crenata.entities.schoolinfo import SchoolInfo


@dataclass
class User(AbstractDomain):
    """
    유저 엔티티입니다.
    """

    preferences: Preferences
    school_info: Optional[SchoolInfo] = field(default=None)
