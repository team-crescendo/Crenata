"""
Crenata의 클라이언트입니다.
"""
from typing import Any

from discord.app_commands.tree import CommandTree
from discord.client import Client
from discord.flags import Intents
from discord.object import Object

from crenata.config import CrenataConfig
from crenata.crenataneispy import CrenataNeispy
from crenata.database import ORM


class Crenata(Client):
    def __init__(
        self, config: CrenataConfig, intents: Intents, *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(intents=intents, *args, **kwargs)
        self.tree = CommandTree(self)
        self.config = config
        self.crenata_neispy = CrenataNeispy.create("")

    async def setup_hook(self) -> None:
        if self.config.PRODUCTION:
            await self.tree.sync()
        else:
            await self.tree.sync(guild=Object(self.config.TEST_GUILD_ID))
        self.orm = await ORM.setup(self.config.DB_URL)

    async def close(self) -> None:
        if self.crenata_neispy.session and not self.crenata_neispy.session.closed:
            await self.crenata_neispy.session.close()
        await self.orm.engine.dispose()
        return await super().close()

    def run(self, *args: Any, **kwargs: Any) -> None:
        """
        Crenata를 실행합니다.

        토큰은 Config에서 로드하기 때문에 인자로 줄 필요가 없습니다.
        """
        kwargs.update({"token": self.config.TOKEN})
        return super().run(*args, **kwargs)
