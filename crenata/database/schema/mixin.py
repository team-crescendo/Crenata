from dataclasses import field

from pydantic.dataclasses import dataclass


@dataclass(validate_on_init=False)
class Schema:
    """
    스키마의 기본 클래스입니다.

    모든 스키마는 이 클래스를 상속받습니다.
    """

    id: int

    class Config:
        orm_mode = True


@dataclass(validate_on_init=False)
class ForeignKeySchema(Schema):
    """
    외래키를 가지는 스키마의 기본 클래스입니다.

    모든 외래키를 가지는 스키마는 이 클래스를 상속받습니다.
    """

    id: int = field(init=False)
    user_id: int
