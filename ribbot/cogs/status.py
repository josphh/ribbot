from itertools import cycle

import discord
from discord.ext import commands, tasks

status = cycle(["f.help", "\\*ribbit\\*", "uwu froggy go croak croak"])


class StatusCycle(commands.Cog):
    """Cog which cycles the bot's status between various messages."""

    def __init__(self, client):
        self.client = client

    @tasks.loop(seconds=10)
    async def change_status(self):
        """Cycle the status message every 10 seconds."""
        await self.client.change_presence(
            status=discord.Status.idle, activity=discord.Game(status)
        )

    @commands.Cog.listener()
    async def on_ready(self):
        """Start cycling the status once the bot has loaded."""
        self.change_status.start()  # pylint: disable=no-member


def setup(client):
    """Add the StatusCycle cog to a Discord client."""
    client.add_cog(StatusCycle(client))
