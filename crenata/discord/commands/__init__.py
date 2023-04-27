from crenata.discord.commands.admin import admin
from crenata.discord.commands.admin.users import users as _
from crenata.discord.commands.exit import exit
from crenata.discord.commands.preferences import preferences
from crenata.discord.commands.preferences.edit import preferences_edit as _
from crenata.discord.commands.profile import profile
from crenata.discord.commands.register import register
from crenata.discord.commands.school import school
from crenata.discord.commands.school.meal import meal as _
from crenata.discord.commands.school.search import search as _
from crenata.discord.commands.school.set import school_set as _
from crenata.discord.commands.school.timetable import time_table as _

commands = [register, profile, exit, school, preferences, admin]
