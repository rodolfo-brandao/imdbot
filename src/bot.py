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
    Logs the running bot.
    '''

    print(f'{bot.user} is online!')


@bot.command(
    name='ping',
    help='Shows the bot latency.'
)
async def get_latency(ctx) -> None:
    '''
    Sends the bot latency in milliseconds.
    '''

    await ctx.send(f'{round(bot.latency * 1000)}ms')


@bot.command(
    name='movies',
    help='Lists all movies whose title/description matches the given argument.'
)
async def get_movies(ctx, *args) -> None:
    '''
    Searches for movies occurences in the IMDb API.
    '''

    search_str = ' '.join(args).lower()
    response = imdb.search(search_str)

    await ctx.send("Just a sec...")

    for item in response:
        movie_id = f'Id: `{item["id"]}`'
        title = f'Title: `{item["title"]}'
        description = f'Description: `{item["description"]}`'
        poster = f'Poster: {item["image_url"]}'

        message = f'{movie_id}\n{title}\n{description}\n{poster}'
        await ctx.send(message)

    await ctx.send("That's all I could find")


@bot.command(
    name='series',
    help='Lists all series whose title/description matches the given argument.'
)
async def get_series(ctx, *args):
    '''
    Searches for series occurences in the IMDb API.
    '''

    search_str = ' '.join(args).lower()
    response = imdb.search(search_str, search_type='series')

    await ctx.send("Just a sec...")

    for item in response:
        series_id = f'Id: `{item["id"]}`'
        title = f'Title: `{item["title"]}'
        description = f'Description: `{item["description"]}`'
        poster = f'Poster: {item["image_url"]}'

        message = f'{series_id}\n{title}\n{description}\n{poster}'
        await ctx.send(message)

    await ctx.send("That's all I could find")


@bot.command(
    name='details',
    help='Lists all movie/series details by the given id.'
)
async def get_details(ctx, arg):
    '''
    Gets all movie/series details provided by the IMDb API.
    '''

    response = imdb.search_title(arg)

    title = f'Title: `{response["title"]}`'
    year = f'Year: `{response["year"]}`'
    runtime = f'Runtime: `{response["runtime"] if response["runtime"] is not None or "" else "?"}`'
    plot = f'Plot: `{response["plot"]}`'
    directors = f'Directors: `{response["directors"] if response["directors"] is not None or "" else "?"}`'
    stars = f'Stars: `{response["stars"] if response["stars"] is not None or "" else "?"}`'
    imdb_rating = f'IMDb Rating: `{response["imdb_rating"]}`'
    imdb_votes = f'IMDb Votes: `{response["imdb_votes"]}`'
    poster = f'Poster: {response["image_url"]}'

    message = f'{title}\n{year}\n{runtime}\n{plot}\n{directors}\n{stars}\n{imdb_rating}\n{imdb_votes}\n{poster}'
    await ctx.send(message)

bot.run(DISCORD_TOKEN)
