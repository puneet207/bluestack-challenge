import discord
from discord.ext import commands
import urllib

# client = discord.Client()
bot = commands.Bot(command_prefix='!')
TOKEN = "NjkwMTM5MTU2MzkwNjA4ODk2.XnNO3A.FWbaRMMKVMzaQn-z_U_qiV4mv00"


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    if message.content.lower() == "hey":
        await message.channel.send("hi")


@bot.command()
async def google(ctx, *, search):
    print("here")
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
        'http://www.google.com/search?q=' + query_string
    )
    search_result = htm_content.read().decode()
    await ctx.send(search_result)


bot.run(TOKEN)
