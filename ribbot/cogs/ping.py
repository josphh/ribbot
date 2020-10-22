from discord.ext import commands


class Ping(commands.Cog):
    """Cog providing a way to check the latency of the bot."""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """Measure the latency of Ribbot's communication with Discord."""
        await ctx.send(f"Pong! ({round(self.client.latency * 1000)}ms)")


def setup(client):
    """Add the Ping cog to a Discord client."""
    client.add_cog(Ping(client))
