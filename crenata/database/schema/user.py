from sqlalchemy.orm import Mapped, relationship

from crenata.database.registry import mapper_registry
from crenata.database.schema.mixin import Schema
from crenata.database.schema.preferences import PreferencesSchema
from crenata.database.schema.schoolinfo import SchoolInfoSchema


@mapper_registry.mapped_as_dataclass
class UserSchema(Schema):
    """
    유저 스키마입니다.
    """

    __tablename__ = "user"

    preferences: Mapped[PreferencesSchema] = relationship(
        uselist=False,
        cascade="all, delete",
        passive_deletes=True,
    )
    school_info: Mapped[SchoolInfoSchema] = relationship(
        uselist=False,
        cascade="all, delete",
        passive_deletes=True,
        default=None,
    )
