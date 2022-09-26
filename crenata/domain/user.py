from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    school_name: Optional[str]

    ATPT_OFCDC_SC_CODE: Optional[str]
    SD_SCHUL_CODE: Optional[str]
