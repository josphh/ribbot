from discord.ext import commands


class Greet(commands.Cog):
    """Cog providing a greeting command."""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def greet(self, ctx):
        """Send a greeting."""
        await ctx.send("\\*ribbit\\* :eye: :tongue: :eye: ")


def setup(client):
    """Add the Greet cog to a Discord client."""
    client.add_cog(Greet(client))
