from argparse import Namespace

from discord import Intents

from crenata.application.client import Crenata
from crenata.application.commands.register import register
from crenata.application.error.callback import error_handler


def create_app(args: Namespace, intents: Intents) -> Crenata:
    crenata = Crenata(intents=intents)
    crenata.config.update_with_args(args)
    crenata.tree.set_error_handler(error_handler)
    crenata.tree.add_command(register)
    return crenata
