from argparse import ArgumentParser
from sys import argv

from discord import Intents, Object

from crenata import create_client
from crenata.argparser import parse_args
from crenata.commands import commands
from crenata.config import CrenataConfig
from crenata.events.error import on_error

if __name__ == "__main__":
    crenata_config = CrenataConfig()
    parser = ArgumentParser("crenata")
    args = parse_args(parser, argv[1:])
    crenata_config.update_with_args(args)
    client = create_client(crenata_config, intents=Intents.default())
    for command in commands:
        if client.config.PRODUCTION:
            client.tree.add_command(command)
        else:
            client.tree.add_command(command, guild=Object(client.config.TEST_GUILD_ID))
    setattr(client.tree, "on_error", on_error)
    client.run()
