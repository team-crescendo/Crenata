from __future__ import annotations

from typing import Optional

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crenata.core.user.domain.entity import User
from crenata.infrastructure.sqlalchemy.base import Base
from crenata.infrastructure.sqlalchemy.mixin import Schema
from crenata.infrastructure.sqlalchemy.preferences.domain.entity import (
    PreferencesSchema,
)
from crenata.infrastructure.sqlalchemy.schoolinfo.domain.entity import SchoolInfoSchema


class UserSchema(Base, Schema):
    """
    유저 스키마입니다.
    """

    __tablename__ = "user"

    discord_id: Mapped[int] = mapped_column(BigInteger)
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

    def to_entity(self) -> User:
        return User(
            discord_id=self.discord_id,
            preferences=self.preferences.to_entity(),
            school_info=(
                self.school_info.to_entity() if self.school_info is not None else None
            ),
        )

    @classmethod
    def from_entity(cls, user: User) -> UserSchema:
        return cls(
            discord_id=user.discord_id,
            preferences=PreferencesSchema.from_entity(user.preferences),
            school_info=(
                SchoolInfoSchema.from_entity(user.school_info)
                if user.school_info is not None
                else None
            ),
        )
