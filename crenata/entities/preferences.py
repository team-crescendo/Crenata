from dataclasses import field

from pydantic.dataclasses import dataclass

from crenata.abc.domain import AbstractDomain


@dataclass(validate_on_init=False)
class Preferences(AbstractDomain):
    """
    환경설정 엔티티입니다.
    """

    private: bool = field(default=True)
    ephemeral: bool = field(default=False)
