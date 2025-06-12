from abc import ABC, abstractmethod
from typing import Optional

from crenata.core.schoolinfo.domain.entity import SchoolInfo


class SchoolInfoRepository(ABC):
    @abstractmethod
    async def get_school_info(self, user_id: int) -> Optional[SchoolInfo]: ...

    @abstractmethod
    async def create_school_info(
        self, user_id: int, school_info: SchoolInfo
    ) -> SchoolInfo: ...

    @abstractmethod
    async def update_school_info(
        self, user_id: int, school_info: SchoolInfo
    ) -> None: ...

    @abstractmethod
    async def delete_school_info(self, user_id: int) -> None: ...
