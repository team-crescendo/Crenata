from dataclasses import dataclass, field

from crenata.abc.domain import AbstractDomain


@dataclass
class Preferences(AbstractDomain):
    """
    환경설정 엔티티입니다.
    """

    private: bool = field(default=True)
    ephemeral: bool = field(default=False)
