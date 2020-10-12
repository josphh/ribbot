import json
import os
import sys

import discord
from discord.ext import commands

# loads the prefix from the json file and allows the user to change it
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix= get_prefix)


## sets default value to '.f'
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'f.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)

    await ctx.send(f'Prefix changed to: ' + prefix)


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
