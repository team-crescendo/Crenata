from abc import ABC

from crenata.core.schoolinfo.domain.entity import SchoolInfo


class SchoolInfoRepository(ABC):
    async def get_schoolinfo(self, user_id: int) -> SchoolInfo:
        ...

    async def create_schoolinfo(self, schoolinfo: SchoolInfo) -> SchoolInfo:
        ...

    async def update_schoolinfo(self, schoolinfo: SchoolInfo) -> SchoolInfo:
        ...

    async def delete_schoolinfo(self, schoolinfo_id: int) -> None:
        ...
