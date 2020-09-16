import discord
import os
import json
from discord.ext import commands

#allows user to change bot prefix
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes =json.load(f)

    return prefixes[str(message.guild.id)]

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes =json.load(f)

    prefixes[str(guild.id)] = 'f.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes =json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f indent=4)


client = commands.Bot(command_prefix = get_prefix)

#error message if a command isn't found
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('\*confused croak\*. Invalid command used')


#runs check for if the user is the bot author
def check_if_me(ctx):
    return ctx.message.author.id == 459820583224606721


#commands to load and unload the cogs in ./cogs
@client.command()
@commands.check(check_if_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('*Cog Loaded*')

@client.command()
@commands.check(check_if_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('*Cog Unloaded*')

@client.command()
@commands.check(check_if_me)
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.send('*Cog Reloaded*')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('secrets.RIBBOT_CLIENT_ID')
