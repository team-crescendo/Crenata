from crenata.abc.command import AbstractCrenataCommand
from crenata.commands.utils import defer
from crenata.discord.interaction import school_page
from crenata.domain.entities.user import User
from crenata.registry import Registry


@Registry.register
class Register(AbstractCrenataCommand):
    @defer
    async def execute(self, school_name: str, grade: int, class_num: int) -> None:
        data = await school_page(self, school_name)
        await self.interaction.client.ctx.query.user.create(
            User(
                id=self.interaction.user.id,
                school_name=data.SCHUL_NM,
                grade=grade,
                class_num=class_num,
                ATPT_OFCDC_SC_CODE=data.ATPT_OFCDC_SC_CODE,
                SD_SCHUL_CODE=data.SD_SCHUL_CODE,
            )
        )
        await self.respond(content="성공적으로 등록되었어요.", embed=None, view=None)
