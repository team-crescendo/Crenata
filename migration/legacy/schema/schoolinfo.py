from migration.legacy.base import Base
from migration.legacy.schema.mixin import ForeignKeySchema
from sqlalchemy.orm import Mapped, mapped_column


class SchoolInfoSchema(Base, ForeignKeySchema):
    __tablename__ = "school_info"
    """
    학교정보 스키마입니다.
    """

    school_name: Mapped[str] = mapped_column()
    grade: Mapped[int] = mapped_column()
    room: Mapped[int] = mapped_column()

    ATPT_OFCDC_SC_CODE: Mapped[str] = mapped_column()
    SD_SCHUL_CODE: Mapped[str] = mapped_column()
