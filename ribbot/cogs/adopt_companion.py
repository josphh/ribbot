import discord
from discord.ext import commands
import json
import os


class Adopt(commands.Cog):
    """Cog providing a way to adopt a companion."""

    def __init__(self, client):
        self.client = client


def setup(client):
    """Add the Adopt cog to a Discord client."""
    client.add_cog(Adopt(client))
