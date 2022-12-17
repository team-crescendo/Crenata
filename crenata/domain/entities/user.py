from pydantic.dataclasses import dataclass

from crenata.abc.domain import AbstractDomain


@dataclass
class User(AbstractDomain):
    id: int
    school_name: str
    grade: int
    class_num: int

    ATPT_OFCDC_SC_CODE: str
    SD_SCHUL_CODE: str

    class Config:
        orm_mode = True
