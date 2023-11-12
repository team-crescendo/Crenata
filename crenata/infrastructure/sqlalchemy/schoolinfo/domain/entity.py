from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from crenata.core.schoolinfo.domain.entity import SchoolInfo
from crenata.infrastructure.sqlalchemy.base import Base
from crenata.infrastructure.sqlalchemy.mixin import ForeignKeySchema


class SchoolInfoSchema(Base, ForeignKeySchema):
    __tablename__ = "school_info"
    """
    학교정보 스키마입니다.
    """

    name: Mapped[str] = mapped_column()
    grade: Mapped[int] = mapped_column()
    room: Mapped[int] = mapped_column()

    edu_office_code: Mapped[str] = mapped_column()
    standard_school_code: Mapped[str] = mapped_column()
    ORD_SC_NM: Mapped[str | None] = mapped_column()
    DDDEP_NM: Mapped[str | None] = mapped_column()

    def to_entity(self) -> SchoolInfo:
        return SchoolInfo(
            name=self.name,
            grade=self.grade,
            room=self.room,
            edu_office_code=self.edu_office_code,
            standard_school_code=self.standard_school_code,
            ORD_SC_NM=self.ORD_SC_NM,
            DDDEP_NM=self.DDDEP_NM,
        )

    @classmethod
    def from_entity(cls, user_id: int, school_info: SchoolInfo) -> SchoolInfoSchema:
        return cls(
            discord_id=user_id,
            name=school_info.name,
            grade=school_info.grade,
            room=school_info.room,
            edu_office_code=school_info.edu_office_code,
            standard_school_code=school_info.standard_school_code,
            ORD_SC_NM=school_info.ORD_SC_NM,
            DDDEP_NM=school_info.DDDEP_NM,
        )
