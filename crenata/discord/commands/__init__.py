from glob import glob
from importlib import import_module
from os.path import split, splitext
from typing import Any

from discord.app_commands import Command, Group


def path_split(path: str) -> list[str]:
    head, tail = split(path)
    if not head:
        return [tail]
    return path_split(head) + [splitext(tail)[0]]


def load_commands(path: str) -> list[Command[Any, ..., Any] | Group]:
    commands: list[Command[Any, ..., Any] | Group] = []
    files = glob(path, recursive=True)

    for file in files:
        if file.endswith("__init__.py"):
            continue

        module = import_module(".".join(path_split(file)))

        for name in dir(module):
            attr = getattr(module, name)

            if isinstance(attr, Command):
                if not attr.parent:
                    commands.append(attr)

            elif isinstance(attr, Group):
                if not attr in commands:
                    commands.append(attr)

    return commands
