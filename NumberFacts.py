import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix="!")

# @client.command()
# async def ISTE(ctx, arg):
#     a = ""
#     for i in range(len(a)):
#         print(arg)
#         print(a)
#         a = a.append(str(arg[i]))
#         print(a)

#     await ctx.send(arg)


@client.command()
async def number(context, arg):
    api_string = 'http://numbersapi.com/' + str(arg) + '/math'
    response = requests.get(api_string)
    await context.send(response.text)




client.run("OTM3OTg2NDM1MDQ5NDU5NzMy.Yfjt8Q.Y2_SxxVn4J3UEo1BY1R3r9wWGwk")
