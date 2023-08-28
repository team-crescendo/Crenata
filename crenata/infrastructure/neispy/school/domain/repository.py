from neispy.client import Neispy

from crenata.core.school.domain.entity import School
from crenata.core.school.domain.repository import SchoolRepository
from crenata.infrastructure.utils.datetime import to_datetime


class SchoolRepositoryImpl(SchoolRepository):
    def __init__(self, neispy: Neispy) -> None:
        self.neispy = neispy

    async def search_school(self, school_name: str) -> list[School]:
        r = await self.neispy.schoolInfo(SCHUL_NM=school_name)
        row = r.schoolInfo[1].row

        return [
            School(
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
            for school in row
        ]
