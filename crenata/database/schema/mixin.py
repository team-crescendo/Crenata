from dataclasses import dataclass

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


@dataclass(kw_only=True)
class Schema:
    """
    스키마의 기본 클래스입니다.

    모든 스키마는 이 클래스를 상속받습니다.
    """

    id: Mapped[int] = mapped_column(primary_key=True)


@dataclass(kw_only=True)
class ForeignKeySchema(Schema):
    """
    외래키를 가지는 스키마의 기본 클래스입니다.

    모든 외래키를 가지는 스키마는 이 클래스를 상속받습니다.
    """

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("user.id", ondelete="CASCADE"), unique=True
    )
