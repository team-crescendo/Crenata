"""
Crenata의 Config입니다.

모든 설정값은 이곳에서 참조되어야합니다.
"""
from argparse import Namespace
from json import loads
from os import environ
from typing import Any, Callable


# distutil.util.strtobool
def strtobool(val: str) -> bool:
    """
    Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif val in ("n", "no", "f", "false", "off", "0"):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))


class CrenataConfig(dict[str, Any]):
    """
    Crenata Config 클래스 입니다.
    """

    USE_ENV: bool
    PRODUCTION: bool
    TEST_GUILD_ID: int
    TOKEN: str
    NEIS_API_KEY: str
    DB_URL: str
    CONFIG: str

    def __init__(self, prefix: str = "CRENATA_"):
        self.prefix = prefix
        self.update(
            {
                "USE_ENV": False,
                "PRODUCTION": False,
                "TEST_GUILD_ID": 0,
                "DB_URL": "",
                "CONFIG": "",
                "TOKEN": "",
                "NEIS_API_KEY": "",
            }
        )
        self.load_environment_vars()

    def __getattr__(self, attr: Any) -> Any:
        return self[attr]

    def __setattr__(self, __name: str, __value: Any) -> None:
        return self.update({__name: __value})

    def load_environment_vars(self) -> None:
        """
        환경변수값을 Config에 로드합니다.
        """
        for key, value in environ.items():
            if key.startswith(self.prefix):
                # 타입 변환
                converters: list[
                    type[int] | type[float] | Callable[[str], bool] | type[str]
                ] = [int, float, strtobool, str]
                for converter in converters:
                    try:
                        self[key[len(self.prefix) :]] = converter(value)
                        break
                    except ValueError:
                        ...

    def load_config_with_config_json(self, path: str) -> None:
        """
        주어진 경로의 json을 Config에 로드합니다.
        """
        with open(path, "r") as f:
            config = loads(f.read())
            self.update(config)
        return None

    def update_with_args(self, args: Namespace) -> None:
        """
        명령줄 인수로 받은 Config값들로 업데이트합니다.

        만약 ``USE_ENV``가 ``True``일경우 명령줄 인수는 무시됩니다.
        """
        if not self.USE_ENV:
            self.update({k.upper(): v for k, v in vars(args).items()})
        if self.CONFIG:
            self.load_config_
