from types import SimpleNamespace
from typing import Any

from crenata.config import CrenataConfig
from crenata.domain.usecase import UseCase
from crenata.neispy import CrenataNeispy
from discord import Client, Intents, Interaction, Object
from discord.app_commands.tree import CommandTree


class Crenata(Client):
    def __init__(self, intents: Intents, *args: Any, **kwargs: Any) -> None:
        super().__init__(intents=intents, *args, **kwargs)
        self.tree = CommandTree(self)
        self.ctx: CrenataContext = CrenataContext()

    async def startup(self):
        self.ctx.query = await UseCase.setup(self.ctx.config.DB_URL)

    async def closeup(self):
        if self.ctx.neispy.session and not self.ctx.neispy.session.closed:
            await self.ctx.neispy.session.close()
        if getattr(self.ctx, "usecase", None):
            await self.ctx.query.orm.engine.dispose()

    async def setup_hook(self) -> None:
        if self.ctx.config.PRODUCTION:
            await self.tree.sync()
        else:
            await self.tree.sync(guild=Object(self.ctx.config.TEST_GUILD_ID))
        await self.closeup()

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
    query: UseCase


class CrenataInteraction(Interaction):
    @property
    def client(self) -> Crenata:
        ...
