import discord
from discord.ext import commands, bridge

from utils.views import HelpSelectMenu
from utils.bot import get_config


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def get_status(self):
        match self.client.status:
            case discord.Status.online:
                return "🟩"
            case discord.Status.idle:
                return "🟨"
            case discord.Status.dnd:
                return "🟥"
            case _:
                return "Unable to retrieve status."

    @bridge.bridge_command(name="help", description="shows explanations of commands")
    async def _help(self, ctx):
        config = await get_config()
        prefix = '!'
        status = await self.get_status()

        embed = discord.Embed(
            title=self.client.user.name,
            description=f"A help menu for {self.client.user.name}. Use the select menu to navigate to a category",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=self.client.user.display_avatar.url)
        embed.add_field(name="Prefix", value=prefix, inline=True)
        embed.add_field(name="Latency", value=f"{self.client.latency * 1000:.0f}ms", inline=True)
        embed.add_field(name="Status", value=status, inline=True)
        embed.set_footer(text=f"Created by: {config['BotInformation']['Developer']}")

        await ctx.respond(embed=embed, view=HelpSelectMenu(self.client, prefix))


def setup(client):
    client.add_cog(HelpCommand(client))
