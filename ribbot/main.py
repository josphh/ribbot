import json
import os
import sys

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="f.")

# error message if a command isn't found
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("\*confused croak\*. Invalid command used")


# commands to load and unload the cogs in ./cogs
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send("*Cog Loaded*")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("*Cog Unloaded*")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send("*Cog Reloaded*")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


try:
    client.run(os.environ["RIBBOT_DISCORD_TOKEN"])
except KeyError:
    print("Please set the environment variable RIBBOT_DISCORD_TOKEN.", file=sys.stderr)
    exit(2)
