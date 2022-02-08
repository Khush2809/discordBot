import discord
# from discord.ext import commands
# from music import music

# client = commands.Bot(command_prefix="!")
client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    msg = message.content.lower()
    if(message.author == client.user):
        return
    else:
        if(msg.startswith("hello") or msg.startswith("hi")):
            await message.channel.send('Hi! ' + str(message.author))

        # abusive content
        if('kill' or 'hate' in msg):
            await message.channel.send("Doesn't matter me ;-) !!")

# @client.command()
# async def hello(ctx):
#     await ctx.send("Hi")

# @client.command()
# async def Hi(ctx):
#     await ctx.send("Hello")

# cogs = [music]

# for i in range(len(cogs)):
#     cogs[i].setup(client)

# client.add_cog(music(client))

client.run("OTM3OTg2NDM1MDQ5NDU5NzMy.Yfjt8Q.MWaaWsqL5uOKIsySTg3CuHANKI4")