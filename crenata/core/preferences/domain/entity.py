from dataclasses import dataclass


@dataclass
class Preferences:
    private: bool
    ephemeral: bool
