from argparse import Namespace

from crenata.application.client import Crenata
from crenata.application.commands.register import register
from crenata.application.commands.school import school
from crenata.application.error.callback import error_handler
from discord import Intents


def create_app(args: Namespace, intents: Intents) -> Crenata:
    crenata = Crenata(intents=intents)
    crenata.config.update_with_args(args)
    crenata.tree.set_error_handler(error_handler)
    crenata.tree.add_command(register)
    crenata.tree.add_command(school)
    return crenata
