from discord import Embed, Interaction, app_commands

from crenata.application.client import Crenata
from crenata.core.user.domain.entity import User
from crenata.core.user.usecases.create import CreateUserUseCase
from crenata.infrastructure.sqlalchemy.user.domain.repository import UserRepositoryImpl


@app_commands.command(name="가입", description="가입합니다.")
async def register(interaction: Interaction[Crenata]) -> None:
    repository = UserRepositoryImpl(interaction.client.database)
    usecase = CreateUserUseCase(repository)
    await usecase.execute(User.default(interaction.user.id))

    embed = Embed(title="가입 완료", description="가입이 완료되었습니다.")

    await interaction.response.send_message(embed=embed, ephemeral=True)
