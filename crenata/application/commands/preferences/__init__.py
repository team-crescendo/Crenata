from discord import app_commands

from crenata.application.commands.preferences.edit import edit

preferences = app_commands.Group(
    name="환경설정", description="환경설정 관련 명령어입니다."
)

preferences.add_command(edit)
