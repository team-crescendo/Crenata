from abc import ABC, abstractmethod
from typing import Any

from crenata.typing import CrenataInteraction


class AbstractCrenataCommand(ABC):
    def __init__(self, interaction: CrenataInteraction) -> None:
        self.interaction = interaction

    @abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> Any:
        ...
