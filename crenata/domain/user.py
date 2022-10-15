from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    school_name: str
    grade: int
    class_num: int

    ATPT_OFCDC_SC_CODE: str
    SD_SCHUL_CODE: str

    class Config:
        orm_mode = True
