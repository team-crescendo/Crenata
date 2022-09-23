"""
MIT License

Copyright (c) 2022 Team Crescendo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from discord import Intents, Object

from crenata.client import Crenata
from crenata.config import CrenataConfig


def create_client(config: CrenataConfig) -> Crenata:
    """
    명령어를 추가하고, Config값을 사용해서 Crenata 클라이언트를 반환합니다.
    """
    crenata = Crenata(config, intents=Intents.default())
    
    # for command in commands:
    #     if config.PRODUCTION:
    #         crenata.tree.add_command(command)
    #     else:
    #         crenata.tree.add_command(command, guild=Object(config.TEST_GUILD_ID))
    return crenata
