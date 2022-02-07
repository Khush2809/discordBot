import discord
from discord.ext import commands
from music import music

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.command()
async def Hi(ctx):
    await ctx.send("Hello")

# cogs = [music]

# for i in range(len(cogs)):
#     cogs[i].setup(client)

client.add_cog(music(client))

client.run("OTM3OTg2NDM1MDQ5NDU5NzMy.Yfjt8Q.O7T-MWiSwIPVw7Hk0SArvQ2WCBw")