from abc import ABC, abstractmethod
from typing import Optional

from crenata.core.majorinfo.domain.entity import MajorInfo


class MajorInfoRepository(ABC):
    @abstractmethod
    async def get_majorinfo(
        self, edu_office_code: str, standard_school_code: str
    ) -> Optional[list[MajorInfo]]: ...
