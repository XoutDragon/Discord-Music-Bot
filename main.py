import discord

import logging
import os

from utils.bot import MusicBot


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("discord")
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)


client = MusicBot()


for directory in ['./commands', './events']:
    for file in os.listdir(directory):
        if file.endswith(".py"):
            client.load_extension(f"{directory}.{file[:-3]}")

if __name__ == "__main__":
    client.run(os.environ["DISCORD_TOKEN"])

