from argparse import Namespace

from discord import Intents

from crenata.application.client import Crenata


def create_app(args: Namespace, intents: Intents) -> Crenata:
    crenata = Crenata(intents=intents)
    crenata.config.update_with_args(args)

    return crenata
