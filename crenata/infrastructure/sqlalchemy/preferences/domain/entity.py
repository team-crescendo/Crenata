from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from crenata.core.preferences.domain.entity import Preferences
from crenata.infrastructure.sqlalchemy.base import Base
from crenata.infrastructure.sqlalchemy.mixin import ForeignKeySchema


class PreferencesSchema(Base, ForeignKeySchema):
    __tablename__ = "preferences"
    """
    환경설정 스키마입니다.
    """

    private: Mapped[bool] = mapped_column(default=True)
    ephemeral: Mapped[bool] = mapped_column(default=False)

    def to_entity(self) -> Preferences:
        return Preferences(private=self.private, ephemeral=self.ephemeral)

    @classmethod
    def from_entity(cls, user_id: int, preferences: Preferences) -> PreferencesSchema:
        return cls(
            discord_id=user_id,
            private=preferences.private,
            ephemeral=preferences.ephemeral,
        )
