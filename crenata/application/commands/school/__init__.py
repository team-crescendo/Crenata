from discord import app_commands

from crenata.application.commands.school.meal import meal

school = app_commands.Group(name="학교", description="학교 관련 명령어입니다.")

school.add_command(meal)
