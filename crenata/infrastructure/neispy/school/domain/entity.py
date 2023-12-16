from dataclasses import dataclass

from neispy.domain.schoolinfo import SchoolInfoRow

from crenata.core.school.domain.entity import School
from crenata.infrastructure.utils.datetime import to_datetime


@dataclass
class SchoolAdapter(School):
    @classmethod
    def from_neispy(cls, school: SchoolInfoRow) -> School:
        return cls(
            edu_office_code=school.ATPT_OFCDC_SC_CODE,
            standard_school_code=school.SD_SCHUL_CODE,
            name=school.SCHUL_NM,
            english_name=school.ENG_SCHUL_NM,
            kind=school.SCHUL_KND_SC_NM,
            coeducation=school.COEDU_SC_NM,
            street_name_address=school.ORG_RDNMA,
            zip_code=school.ORG_RDNZC,
            highschool_general_or_business=school.HS_GNRL_BUSNS_SC_NM,
            highschool_category=school.HS_SC_NM,
            fax_number=school.ORG_FAXNO,
            telephone_number=school.ORG_TELNO,
            homepage_address=school.HMPG_ADRES,
            founding_date=to_datetime(school.FOND_YMD),
        )
