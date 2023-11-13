from argparse import Namespace

from discord import Intents

from crenata.application.client import Crenata
from crenata.application.commands.exit import exit
from crenata.application.commands.preferences import preferences
from crenata.application.commands.register import register
from crenata.application.commands.school import school
from crenata.application.error.callback import error_handler


def create_app(args: Namespace, intents: Intents) -> Crenata:
    crenata = Crenata(intents=intents)
    crenata.config.update_with_args(args)
    crenata.tree.set_error_handler(error_handler)
    crenata.tree.add_command(register)
    crenata.tree.add_command(exit)
    crenata.tree.add_command(school)
    crenata.tree.add_command(preferences)
    return crenata
