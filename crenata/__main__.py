from argparse import ArgumentParser
from sys import argv

from discord import Intents

from crenata.application import create_app
from crenata.infrastructure.utils.argparser import parse_args

if __name__ == "__main__":
    parser = ArgumentParser("crenata")
    args = parse_args(parser, argv[1:])

    client = create_app(args, intents=Intents.default())

    client.run()
