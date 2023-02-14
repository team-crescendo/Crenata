from pydantic.dataclasses import dataclass

from crenata.abc.domain import AbstractDomain


@dataclass(validate_on_init=False)
class SchoolInfo(AbstractDomain):
    """
    학교정보 엔티티입니다.
    """

    school_name: str
    grade: int
    room: int

    ATPT_OFCDC_SC_CODE: str
    SD_SCHUL_CODE: str
