from sqlalchemy.orm import Mapped, mapped_column

from crenata.database.base import Base
from crenata.database.schema.mixin import ForeignKeySchema



class PreferencesSchema(Base, ForeignKeySchema):
    __tablename__ = "preferences"
    """
    환경설정 스키마입니다.
    """

    private: Mapped[bool] = mapped_column(default=True)
    ephemeral: Mapped[bool] = mapped_column(default=False)
