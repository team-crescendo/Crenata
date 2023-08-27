from dataclasses import dataclass
from datetime import datetime


@dataclass
class Meal:
    name: str
    """식사명"""
    dish_name: str
    """요리명"""
    school_name: str
    """학교명"""
    calorie: str
    """칼로리"""
    date: datetime
    """급식일자"""
