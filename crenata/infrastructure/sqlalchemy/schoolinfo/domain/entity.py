from sqlalchemy.orm import Mapped, mapped_column

from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.infrastructure.sqlalchemy.base import Base
from crenata.infrastructure.sqlalchemy.mixin import ForeignKeySchema


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
    ORD_SC_NM: Mapped[str | None] = mapped_column()
    DDDEP_NM: Mapped[str | None] = mapped_column()

    def to_entity(self):
        return SchoolInfo(
            school_name=self.school_name,
            grade=self.grade,
            room=self.room,
            ATPT_OFCDC_SC_CODE=self.ATPT_OFCDC_SC_CODE,
            SD_SCHUL_CODE=self.SD_SCHUL_CODE,
            ORD_SC_NM=self.ORD_SC_NM,
            DDDEP_NM=self.DDDEP_NM,
        )

    @classmethod
    def from_entity(cls, school_info: SchoolInfo):
        return cls(
            school_name=school_info.school_name,
            grade=school_info.grade,
            room=school_info.room,
            ATPT_OFCDC_SC_CODE=school_info.ATPT_OFCDC_SC_CODE,
            SD_SCHUL_CODE=school_info.SD_SCHUL_CODE,
            ORD_SC_NM=school_info.ORD_SC_NM,
            DDDEP_NM=school_info.DDDEP_NM,
        )
