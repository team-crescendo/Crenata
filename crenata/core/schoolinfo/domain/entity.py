from dataclasses import dataclass
from typing import Optional


@dataclass
class SchoolInfo:
    school_name: str
    """학교명"""
    grade: int
    """학년"""
    room: int
    """반"""
    edu_office_code: str
    """시도교육청코드"""
    standard_school_code: str
    """표준학교코드"""

    # 수정필요
    ORD_SC_NM: Optional[str]
    """계열명"""
    DDDEP_NM: Optional[str]
    """학과명"""
