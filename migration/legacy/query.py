from migration.legacy import Database
from migration.legacy.repository import *


class Query:
    """
    쿼리 클래스는 데이터베이스에 접근하는 모든 클래스를 관리합니다.

    레포지토리 클래스를 접근할 수 있도록 합니다.
    """

    def __init__(self, database: Database) -> None:
        self.database = database

    @classmethod
    async def setup(cls, db_url: str) -> "Query":
        return cls(await Database.setup(db_url))

    @property
    def user(self) -> UserRepository:
        """
        유저 레포지토리를 반환합니다.
        """
        return UserRepository(self.database)

    @property
    def school_info(self) -> SchoolInfoRepository:
        """
        학교 정보 레포지토리를 반환합니다.
        """
        return SchoolInfoRepository(self.database)

    @property
    def preferences(self) -> PreferencesRepository:
        """
        환경설정 레포지토리를 반환합니다.
        """
        return PreferencesRepository(self.database)
