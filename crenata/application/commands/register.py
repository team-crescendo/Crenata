from discord import Embed, Interaction, app_commands

from crenata.application.client import Crenata
from crenata.application.strings import ApplicationStrings
from crenata.core.user.domain.entity import User
from crenata.core.user.usecases.create import CreateUserUseCase
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="가입", description="가입합니다.")
async def register(interaction: Interaction[Crenata]) -> None:
    user_repository = UserRepositoryImpl(interaction.client.database)
    create_user_usecase = CreateUserUseCase(user_repository)

    await create_user_usecase.execute(User.default(interaction.user.id))

    embed = Embed(title=ApplicationStrings.REGISTER_COMPLETED)

    await interaction.response.send_message(embed=embed, ephemeral=True)
