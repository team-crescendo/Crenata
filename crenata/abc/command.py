from abc import ABC, abstractmethod
from typing import Any

from discord import Interaction


class AbstractCrenataCommand(ABC):
    def __init__(self, interaction: Interaction) -> None:
        self.interaction = interaction

    @abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> Any:
        ...
