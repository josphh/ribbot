import json
import os
import sys

from discord.ext import commands


def get_prefix(_, message):
    """Load the prefix from prefixes.json."""
    with open("prefixes.json", "r") as prefixes_file:
        prefixes = json.load(prefixes_file)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)


@client.event
async def on_guild_join(guild):
    """Set default prefix to '.f'."""
    with open("prefixes.json", "r") as prefixes_file:
        prefixes = json.load(prefixes_file)

    prefixes[str(guild.id)] = "f."

    with open("prefixes.json", "w") as prefixes_file:
        json.dump(prefixes, prefixes_file)


@client.event
async def on_guild_remove(guild):
    """Delete prefix setting when the bot is removed from a guild."""
    with open("prefixes.json", "r") as prefixes_file:
        prefixes = json.load(prefixes_file)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as prefixes_file:
        json.dump(prefixes, prefixes_file)


@client.command()
async def changeprefix(ctx, prefix):
    """Change prefix for the given context."""
    with open("prefixes.json", "r") as prefixes_file:
        prefixes = json.load(prefixes_file)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as prefixes_file:
        json.dump(prefixes, prefixes_file)

    await ctx.send("Prefix changed to: " + prefix)


@client.event
async def on_command_error(ctx, error):
    """Send an error message if a command isn't found."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("\\*confused croak\\*. Invalid command used")


# commands to load and unload the cogs in ./cogs
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    """Load a cog from ./cogs."""
    client.load_extension(f"cogs.{extension}")
    await ctx.send("*Cog Loaded*")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    """Unload a cog from ./cogs."""
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("*Cog Unloaded*")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    """Reload a cog from ./cogs."""
    client.reload_extension(f"cogs.{extension}")
    await ctx.send("*Cog Reloaded*")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


try:
    client.run(os.environ["RIBBOT_DISCORD_TOKEN"])
except KeyError:
    print("Please set the environment variable RIBBOT_DISCORD_TOKEN.", file=sys.stderr)
    sys.exit(2)
