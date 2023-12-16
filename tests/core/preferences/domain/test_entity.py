from crenata.core.preferences.domain.entity import Preferences


def test_preferences():
    preferences = Preferences(
        private=True,
        ephemeral=True,
    )

    assert preferences.private == True
    assert preferences.ephemeral == True
