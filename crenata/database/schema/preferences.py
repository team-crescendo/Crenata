from sqlalchemy.orm import Mapped, mapped_column

from crenata.database.registry import mapper_registry
from crenata.database.schema.mixin import ForeignKeySchema


@mapper_registry.mapped_as_dataclass
class PreferencesSchema(ForeignKeySchema):
    __tablename__ = "preferences"
    """
    환경설정 스키마입니다.
    """

    private: Mapped[bool] = mapped_column(default=True)
    ephemeral: Mapped[bool] = mapped_column(default=False)
