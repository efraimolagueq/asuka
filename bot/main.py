from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
from discord.ext import commands
import os, random

client = commands.Bot(command_prefix=".")
package_dir = os.path.dirname(os.path.abspath(__file__))
token = os.getenv("DISCORD_BOT_TOKEN")
scheduler = AsyncIOScheduler({'apscheduler.timezone': 'America/Mexico_City'})


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Amando las waifus .help"))


@client.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong con {str(round(client.latency, 2))} de latencia")


@client.command(name="quiensoy")
async def quiensoy(ctx):
    await ctx.send(f"Tu eres {ctx.message.author.name}")


# @tasks.loop(hours=24)
# async def called_once_a_day():
#     message_channel = client.get_channel()
#     print(f"Got channel {message_channel}")
#     await message_channel.send("feliz domingo")

# async def called_once_a_day():
#     channels = client.get_all_channels()
#     message_channel = None
#     for channel in channels:
#         if channel.name == 'general':
#             message_channel = channel
#     if message_channel is None:
#         message_channel = client.get_channel()
#
#     await message_channel.send("feliz domingo")
# scheduler.add_job(feliz_jueves, 'cron', day_of_week='thu', hour=0, minute=0)


def get_general_channel():
    channels = client.get_all_channels()
    message_channel = None
    for channel in channels:
        if channel.name == 'general':
            message_channel = channel
    if message_channel is None:
        message_channel = channels[0]
    return message_channel


def select_random_dia(dia):
    if dia == 'jueves':
        imagenes = os.path.join(package_dir, 'images/asuka/')
    else:
        imagenes = os.path.join(package_dir, 'images/shrek/')
    rdn_image = random.choice(os.listdir(imagenes))
    return os.path.join(imagenes, rdn_image)


async def feliz_jueves():
    message_channel = get_general_channel()
    await message_channel.send("Feliz Jueves Bakaa!!! <3 @everyone", file=discord.File(select_random_dia('jueves')))


async def feliz_viernes():
    message_channel = get_general_channel()
    await message_channel.send("Gracias a Shrek es viernes!!! @everyone",
                               file=discord.File(select_random_dia('viernes')))


scheduler.add_job(feliz_jueves, 'cron', day_of_week='thu', hour=0, minute=1)
scheduler.add_job(feliz_viernes, 'cron', day_of_week='fri', hour=0, minute=1)

scheduler.start()
client.run(token)

