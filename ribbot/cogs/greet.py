import discord
from discord.ext import commands


class Greet(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def greet(self, ctx):
        await ctx.send("\*ribbit\* :eye: :tongue: :eye: ")


def setup(client):
    client.add_cog(Greet(client))
