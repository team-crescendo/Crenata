from abc import ABC, abstractmethod

from crenata.core.schoolinfo.domain.entity import SchoolInfo


class SchoolInfoRepository(ABC):
    @abstractmethod
    async def get_schoolinfo(self, user_id: int) -> SchoolInfo:
        ...

    @abstractmethod
    async def create_schoolinfo(self, schoolinfo: SchoolInfo) -> SchoolInfo:
        ...

    @abstractmethod
    async def update_schoolinfo(self, schoolinfo: SchoolInfo) -> SchoolInfo:
        ...

    @abstractmethod
    async def delete_schoolinfo(self, schoolinfo_id: int) -> None:
        ...
