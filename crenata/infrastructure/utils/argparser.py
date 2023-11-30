"""
명령줄 인수를 파싱하는 모듈입니다.
"""
from argparse import ArgumentParser, Namespace


def parse_args(parser: ArgumentParser, argv: list[str]) -> Namespace:
    """
    주어진 인수를 파싱합니다.
    """
    config = parser.add_argument_group("config")

    config.add_argument("--token", type=str, default="", help="디스코드 봇 토큰입니다. (기본값: '')")

    config.add_argument(
        "--neis-api-key",
        type=str,
        default="",
        help="open.neis.go.kr의 API 키입니다. (기본값: '')",
    )

    config.add_argument(
        "--test-guild-id",
        type=int,
        default=0,
        help="테스트할 길드 ID입니다. (기본값: 0)",
    )

    config.add_argument(
        "--production",
        action="store_true",
        default=False,
        help="Crenata을 프로덕션 모드로 실행합니다. (기본값: False)",
    )

    config.add_argument(
        "--db-url",
        type=str,
        default="sqlite+aiosqlite:///:memory:",
        help="SQLAlchemy에서 사용하는 DB URL입니다. (기본값: 'sqlite+aiosqlite:///:memory:')",
    )

    config.add_argument(
        "--config",
        type=str,
        default="",
        help="Config 파일의 경로입니다. (기본값: '')",
    )

    return parser.parse_args(argv)
