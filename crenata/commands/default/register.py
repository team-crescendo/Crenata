from crenata.abc.command import AbstractCrenataCommand
from crenata.domain.user import User
from crenata.interaction import school_page


class Register(AbstractCrenataCommand):
    async def execute(  # pyright: ignore [reportIncompatibleMethodOverride]
        self, school_name: str, grade: int, class_num: int
    ) -> None:
        data = await school_page(self.interaction, school_name)
        await self.interaction.client.orm.create_user(
            User(
                id=self.interaction.user.id,
                school_name=data.SCHUL_NM,
                grade=grade,
                class_num=class_num,
                ATPT_OFCDC_SC_CODE=data.ATPT_OFCDC_SC_CODE,
                SD_SCHUL_CODE=data.SD_SCHUL_CODE,
            )
        )
        await self.interaction.edit_original_response(
            content="성공적으로 등록되었어요.", embed=None, view=None
        )
