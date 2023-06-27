from dataclasses import dataclass
from typing import Optional


@dataclass
class SchoolInfo:
    school_name: str
    grade: int
    room: int

    ATPT_OFCDC_SC_CODE: str
    SD_SCHUL_CODE: str
    ORD_SC_NM: Optional[str]
    DDDEP_NM: Optional[str]
