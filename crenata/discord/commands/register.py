from crenata.database.schema.preferences import PreferencesSchema
from crenata.database.schema.user import UserSchema
from crenata.discord import CrenataInteraction
from crenata.utils.discord import InteractionLock
from discord import app_commands


@app_commands.command(name="가입", description="가입합니다.") # type: ignore[arg-type]
async def register(interaction: CrenataInteraction) -> None:
    async with InteractionLock(interaction):
        user = await interaction.client.ctx.query.user.read(interaction.user.id)

        if user:
            await interaction.response.send_message(
                content="이미 가입되어있어요.", ephemeral=True
            )
            return

        user = UserSchema(
            id=interaction.user.id,
            preferences=PreferencesSchema(
                user_id=interaction.user.id,
            ),
        )

        await interaction.client.ctx.query.user.create(user)

        await interaction.response.send_message(
            content="성공적으로 가입되었어요.",
            ephemeral=True,
        )
