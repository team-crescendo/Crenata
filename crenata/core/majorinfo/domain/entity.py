from dataclasses import dataclass
from typing import Optional


@dataclass
class MajorInfo:
    department: Optional[str]
    """계열명"""
    major: Optional[str]
    """학과명"""
