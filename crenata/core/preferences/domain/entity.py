from dataclasses import dataclass


@dataclass
class Preferences:
    private: bool
    ephemeral: bool

    @classmethod
    def default(cls):
        return cls(
            private=True,
            ephemeral=True,
        )
