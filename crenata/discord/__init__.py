from types import SimpleNamespace
from typing import Any, cast

from crenata.config import CrenataConfig
from crenata.database.query import Query
from crenata.neispy import CrenataNeispy
from discord import Client, Intents, Interaction, Object
from discord.app_commands.tree import CommandTree


class Crenata(Client):
    def __init__(self, intents: Intents, *args: Any, **kwargs: Any) -> None:
        super().__init__(intents=intents, *args, **kwargs)
        self.tree = CommandTree(self)
        self.ctx: CrenataContext = CrenataContext()

    async def startup(self) -> None:
        self.ctx.query = await Query.setup(self.ctx.config.DB_URL)

    async def closeup(self) -> None:
        if self.ctx.neispy.session and not self.ctx.neispy.session.closed:
            await self.ctx.neispy.session.close()
        if getattr(self.ctx, "query", None):
            await self.ctx.query.database.engine.dispose()

    async def setup_hook(self) -> None:
        if self.ctx.config.PRODUCTION:
            await self.tree.sync()
        else:
            await self.tree.sync(guild=Object(self.ctx.config.TEST_GUILD_ID))
        await self.startup()

    async def close(self) -> None:
        await self.closeup()
        return await super().close()

    def run(self, *args: Any, **kwargs: Any) -> None:
        """
        Crenata를 실행합니다.

        토큰은 Config에서 로드하기 때문에 인자로 줄 필요가 없습니다.
        """
        kwargs.update({"token": self.ctx.config.TOKEN})
        return super().run(*args, **kwargs)


class CrenataContext(SimpleNamespace):
    neispy: CrenataNeispy
    config: CrenataConfig
    query: Query


class CrenataInteraction(Interaction):
    @property
    def client(self) -> Crenata:
        return cast(Crenata, super().client)
