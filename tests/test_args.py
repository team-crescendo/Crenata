from argparse import ArgumentParser

from crenata.argparser import parse_args
from crenata.config import CrenataConfig


def test_parse_args() -> None:
    config = CrenataConfig()
    args = parse_args(
        ArgumentParser(),
        [
            "--production",
            "--test-guild-id",
            "123456789",
            "--db-url",
            "sqlite:///test.db",
            "--token",
            "token",
            "--neis-api-key",
            "neis",
        ],
    )
    config.update_with_args(args)
    assert config.PRODUCTION
    assert config.TEST_GUILD_ID == 123456789
    assert config.DB_URL == "sqlite:///test.db"
    assert config.TOKEN == "token"
    assert config.NEIS_API_KEY == "neis"


def test_parse_args_with_config() -> None:
    config = CrenataConfig()
    args = parse_args(
        ArgumentParser(),
        ["--config", "tests/config.json"],
    )
    config.update_with_args(args)
    assert config.PRODUCTION
    assert config.TEST_GUILD_ID == 123456789012345678
    assert config.DB_URL == "sqlite:///test.db"
    assert config.TOKEN == "token"
    assert config.NEIS_API_KEY == "neis"
