import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from imdb import Imdb

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
IMDB_API_KEY = os.getenv('IMDB_API_KEY')

imdb = Imdb(IMDB_API_KEY)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready() -> None:
    '''
    Shows the running bot.
    '''

    print(f'Logged as {bot.user}')


@bot.command(name='ping')
async def get_latency(ctx) -> None:
    '''
    Sends the bot latency in milliseconds.
    '''

    await ctx.send(f'{round(bot.latency * 1000)}ms')

bot.run(DISCORD_TOKEN)
