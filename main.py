import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def test(ctx): 
  await ctx.send("testing successful!")
  
token = os.environ.get("TOKEN")
client.run(token)