from discord import app_commands
from discord.interactions import Interaction

from crenata.application.client import Crenata
from crenata.application.strings import ApplicationStrings
from crenata.application.utils import InteractionLock
from crenata.core.preferences.domain.entity import Preferences
from crenata.core.preferences.usecases.update import UpdatePreferencesUseCase
from crenata.infrastructure.sqlalchemy.preferences.domain.repository import (
    PreferencesRepositoryImpl,
)


@app_commands.command(name="변경", description="환경설정을 변경합니다.")
@app_commands.describe(private="학교 이름을 비공개로 할지 여부입니다.")
@app_commands.describe(ephemeral="자기 자신에게만 보이게 할지 여부입니다.")
async def edit(
    interaction: Interaction[Crenata], private: bool, ephemeral: bool
) -> None:
    async with InteractionLock(interaction):
        preferences_repository = PreferencesRepositoryImpl(interaction.client.database)
        update_preferences_usecase = UpdatePreferencesUseCase(preferences_repository)

        await update_preferences_usecase.execute(
            interaction.user.id,
            Preferences(
                private,
                ephemeral,
            ),
        )

        await interaction.response.send_message(
            content=ApplicationStrings.PREFERENCE_EDITED, ephemeral=True
        )
