from neispy.client import Neispy

from crenata.core.school.domain.entity import School
from crenata.core.school.domain.repository import SchoolRepository
from crenata.infrastructure.neispy.school.domain.entity import SchoolAdapter


class SchoolRepositoryImpl(SchoolRepository):
    def __init__(self, neispy: Neispy) -> None:
        self.neispy = neispy

    async def search_school(self, school_name: str) -> list[School]:
        r = await self.neispy.schoolInfo(SCHUL_NM=school_name)
        row = r.schoolInfo[1].row

        return [SchoolAdapter.from_neispy(school) for school in row]
