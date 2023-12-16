from typing import Optional

from migration.legacy.base import Base
from migration.legacy.schema.mixin import Schema
from migration.legacy.schema.preferences import PreferencesSchema
from migration.legacy.schema.schoolinfo import SchoolInfoSchema
from sqlalchemy.orm import Mapped, relationship


class UserSchema(Base, Schema):
    """
    유저 스키마입니다.
    """

    __tablename__ = "user"

    preferences: Mapped[PreferencesSchema] = relationship(
        uselist=False,
        cascade="all, delete",
        passive_deletes=True,
    )
    school_info: Mapped[Optional[SchoolInfoSchema]] = relationship(
        uselist=False,
        cascade="all, delete",
        passive_deletes=True,
        default=None,
    )
