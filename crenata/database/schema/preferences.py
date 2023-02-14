from pydantic.dataclasses import dataclass

from crenata.database.schema.mixin import ForeignKeySchema
from crenata.entities.preferences import Preferences


@dataclass(validate_on_init=False)
class PreferencesSchema(Preferences, ForeignKeySchema):
    """
    환경설정 스키마입니다.
    """

    def to_entity(self) -> Preferences:
        """
        스키마를 엔티티로 변환합니다.
        """
        return Preferences(
            private=self.private,
            ephemeral=self.ephemeral,
        )
