from argparse import ArgumentParser
from sys import argv

from crenata import create_client
from crenata.argparser import parse_args
from crenata.config import CrenataConfig

if __name__ == "__main__":
    crenata_config = CrenataConfig()
    parser = ArgumentParser("crenata")
    args = parse_args(parser, argv[1:])
    crenata_config.update_with_args(args)
    client = create_client(crenata_config)
    client.run()
