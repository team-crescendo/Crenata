from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Preferences:
    private: bool
    ephemeral: bool

    @classmethod
    def default(cls) -> Preferences:
        return cls(private=True, ephemeral=True)
