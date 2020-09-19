from itertools import cycle

import discord
from discord.ext import commands, tasks

status = cycle(["f.help", "*ribbit*", "uwu froggy go croak croak"])


class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.change_presence(
            status=discord.Status.idle, activity=discord.Game(next(status))
        )

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print("Bot is online.")


def setup(client):
    client.add_cog(OnReady(client))
