from discord.ext import commands

bot = commands.Bot(command_prefix='?')
bot.lavanodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_url': f'http://lava.link:{port}'
    }
    ]
@bot.event
async def on_ready():
    print("farding")
    bot.load_extension('dismusic')

bot.run("OTQ2MDY4NzUzOTQ1MzQxOTUy.YhZVMA.ednQG5i1PEryfVHvRyYHJtpgIVg")
