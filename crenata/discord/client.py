from crenata.config import CrenataConfig
from crenata.discord import Crenata
from crenata.neispy import CrenataNeispy
from discord import Intents


def create_client(config: CrenataConfig, *, intents: Intents) -> Crenata:
    client = Crenata(intents=intents)
    client.ctx.config = config
    client.ctx.neispy = CrenataNeispy.create(config.NEIS_API_KEY)
    return client
