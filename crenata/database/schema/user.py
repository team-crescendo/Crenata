from dataclasses import dataclass, field
from typing import Optional

from crenata.database.schema.mixin import Schema
from crenata.database.schema.preferences import PreferencesSchema
from crenata.database.schema.schoolinfo import SchoolInfoSchema
from crenata.entities.user import User


@dataclass
class UserSchema(User, Schema):
    """
    유저 스키마입니다.
    """

    preferences: PreferencesSchema
    school_info: Optional[SchoolInfoSchema] = field(default=None)
