from crenata.application.commands.school.meal import meal
from crenata.application.commands.school.search import search
from crenata.application.commands.school.setup import setup
from crenata.application.commands.school.timetable import timetable
from crenata.application.commands.school.users import users
from discord import app_commands

school = app_commands.Group(name="학교", description="학교 관련 명령어입니다.")

school.add_command(meal)
school.add_command(search)
school.add_command(setup)
school.add_command(users)
school.add_command(timetable)
