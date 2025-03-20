from __future__ import annotations

from typing import Any

from discord import Client, Intents, Object
from neispy import Neispy

from crenata.application.tree import CrenataCommandTree
from crenata.infrastructure.sqlalchemy import Database
from crenata.infrastructure.utils.config import CrenataConfig


class Crenata(Client):
    def __init__(self, intents: Intents, *args: Any, **kwargs: Any) -> None:
        super().__init__(intents=intents, *args, **kwargs)

        self.tree = CrenataCommandTree(self)
        self.config = CrenataConfig()

    async def startup(self) -> None:
        self.neispy = Neispy(self.config.NEIS_API_KEY)
        self.database = await Database.setup(self.config.DB_URL)

    async def closeup(self) -> None:
        if self.neispy.session and not self.neispy.session.closed:
            await self.neispy.session.close()

        if getattr(self, "database", None):
            await self.database.engine.dispose()

    async def setup_hook(self) -> None:
        if self.config.PRODUCTION:
            await self.tree.sync()
        else:
            test_guild = Object(self.config.TEST_GUILD_ID)
            self.tree.copy_global_to(guild=test_guild)
            await self.tree.sync(guild=test_guild)

    async def close(self) -> None:
        await self.closeup()

        return await super().close()

    async def start(self, token: str, *, reconnect: bool = True) -> None:
        await self.startup()

        return await super().start(token, reconnect=reconnect)

    def run(self, *args: Any, **kwargs: Any) -> None:
        """
        Crenata를 실행합니다.

        토큰은 Config에서 로드하기 때문에 인자로 줄 필요가 없습니다.
        """
        kwargs.update({"token": self.config.TOKEN})

        return super().run(*args, **kwargs)
