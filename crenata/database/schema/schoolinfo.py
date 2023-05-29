from sqlalchemy.orm import Mapped, mapped_column

from crenata.database.registry import mapper_registry
from crenata.database.schema.mixin import ForeignKeySchema


@mapper_registry.mapped_as_dataclass
class SchoolInfoSchema(ForeignKeySchema):
    __tablename__ = "school_info"
    """
    학교정보 스키마입니다.
    """

    school_name: Mapped[str] = mapped_column()
    grade: Mapped[int] = mapped_column()
    room: Mapped[int] = mapped_column()

    ATPT_OFCDC_SC_CODE: Mapped[str] = mapped_column()
    SD_SCHUL_CODE: Mapped[str] = mapped_column()
