from abc import ABC

import discord
from discord.ext import bridge

import aiohttp
import logging
import yaml


async def get_config():
    with open('./config.yaml') as f:
        return yaml.safe_load(f)


class MusicBot(bridge.Bot, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix='!',
            case_insensitive=True,
            strip_after_prefix=True,
            activity=discord.Activity(
                type=discord.ActivityType.listening, name=f"/help"
            ),
            help_command=None,
        )
        self.session = None

    async def close(self):
        await super().close()
        await self.session.close()

    async def on_connect(self):
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()

    async def on_ready(self):
        logging.info("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        logging.info(f'Connected to bot: {self.user.name}'.center(55))
        logging.info(f'Bot ID: {self.user.id}'.center(55))
        logging.info("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
