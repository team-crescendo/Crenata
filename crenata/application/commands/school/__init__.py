from discord import app_commands

from crenata.application.commands.school.meal import meal
from crenata.application.commands.school.search import search
from crenata.application.commands.school.setup import setup

school = app_commands.Group(name="학교", description="학교 관련 명령어입니다.")

school.add_command(meal)
school.add_command(search)
school.add_command(setup)
