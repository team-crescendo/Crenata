from dataclasses import dataclass

from neispy.domain.elstimetable import ElsTimeTableRow
from neispy.domain.histimetable import HisTimeTableRow
from neispy.domain.mistimetable import MisTimeTableRow
from neispy.domain.spstimetable import SpsTimeTableRow

from crenata.core.timetable.domain.entity import Timetable
from crenata.infrastructure.utils.datetime import to_datetime


@dataclass
class TimetableAdapter(Timetable):
    @classmethod
    def from_neispy(
        cls,
        timetable: ElsTimeTableRow
        | MisTimeTableRow
        | HisTimeTableRow
        | SpsTimeTableRow,
    ) -> Timetable:
        return cls(subject=timetable.ITRT_CNTNT, date=to_datetime(timetable.ALL_TI_YMD))
