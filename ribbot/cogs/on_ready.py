from discord.ext import commands


class OnReady(commands.Cog):
    """Cog handling log messages during bot startup."""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """Log a message when the bot is loaded."""
        print("Bot is online.")


def setup(client):
    """Add the OnReady cog to a Discord client."""
    client.add_cog(OnReady(client))
