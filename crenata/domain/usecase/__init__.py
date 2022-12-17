from crenata.database import ORM
from crenata.domain.usecase.user import DAOUser


class UseCase:
    def __init__(self, orm: ORM) -> None:
        self.orm = orm

    @classmethod
    async def setup(cls, db_url: str):
        return cls(await ORM.setup(db_url))

    @property
    def user(self):
        return DAOUser(self.orm)
