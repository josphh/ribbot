import discord
from discord.ext import tasks
from itertools import cycle

status = cycle(['f.help', '\*ribbit\*', 'uwu froggy go croak croak'])

class Status_cycle(tasks.Cog):

	def __init__(self, client):
		self.client = client



@tasks.loop(seconds=10)
async def change_status(self):
	await self.client.change_presence(status=discord.Status.idle, activity=discord.Game(status))


def setup(client):
	client.add_cog(Greet(client))
