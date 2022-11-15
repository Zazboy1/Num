import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event 
async def on_ready():
  print('Is read:')
  print(client.user.id, client.user)

@client.command()
async def ping(ctx):
  await ctx.send('pong')
  
client.run('MTAzNDUxOTA4NTI4MDY2NTY2MQ.Gi3Kda.nCPw3BSMNVY11QiI5e5SRDvL5Sq2fNTS8CObks')
