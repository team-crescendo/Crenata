from typing import Optional

from neispy.client import Neispy
from neispy.error import DataNotFound

from crenata.core.majorinfo.domain.entity import MajorInfo
from crenata.core.majorinfo.domain.repository import MajorInfoRepository
from crenata.infrastructure.neispy.majorinfo.domain.entity import MajorInfoAdapter


class MajorInfoRepositoryImpl(MajorInfoRepository):
    def __init__(self, neispy: Neispy) -> None:
        self.neispy = neispy

    async def get_majorinfo(
        self, edu_office_code: str, standard_school_code: str
    ) -> Optional[list[MajorInfo]]:
        try:
            r = await self.neispy.schoolMajorinfo(
                ATPT_OFCDC_SC_CODE=edu_office_code,
                SD_SCHUL_CODE=standard_school_code,
            )

        except DataNotFound:
            return None

        row = r.schoolMajorinfo[1].row

        return [MajorInfoAdapter.from_neispy(majorinfo) for majorinfo in row]
