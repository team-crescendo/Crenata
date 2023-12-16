from dataclasses import dataclass

from neispy.domain.schoolmajorinfo import SchoolMajorInfoRow

from crenata.core.majorinfo.domain.entity import MajorInfo


@dataclass
class MajorInfoAdapter(MajorInfo):
    @classmethod
    def from_neispy(cls, majorinfo: SchoolMajorInfoRow) -> MajorInfo:
        return cls(major=majorinfo.DDDEP_NM, department=majorinfo.ORD_SC_NM)
