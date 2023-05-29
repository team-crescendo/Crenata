from dataclasses import dataclass

from crenata.database.schema.mixin import ForeignKeySchema
from crenata.entities.schoolinfo import SchoolInfo


@dataclass
class SchoolInfoSchema(SchoolInfo, ForeignKeySchema):
    """
    학교정보 스키마입니다.
    """

    def to_entity(self) -> SchoolInfo:
        """
        스키마를 엔티티로 변환합니다.
        """
        return SchoolInfo(
            school_name=self.school_name,
            grade=self.grade,
            room=self.room,
            ATPT_OFCDC_SC_CODE=self.ATPT_OFCDC_SC_CODE,
            SD_SCHUL_CODE=self.SD_SCHUL_CODE,
        )
