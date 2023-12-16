from dataclasses import dataclass
from datetime import datetime


@dataclass
class Timetable:
    subject: str
    date: datetime
