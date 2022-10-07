from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    school_name: str

    ATPT_OFCDC_SC_CODE: str
    SD_SCHUL_CODE: str

    class Config:
        orm_mode = True
