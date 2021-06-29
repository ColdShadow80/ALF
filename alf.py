import discord
import os
import configparser
import asyncio
import subprocess

from discord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['GENERAL']['TOKEN']
ADMIN = config['GENERAL']['ADMIN']
PREFIX = config['GENERAL']['PREFIX']
SCRIPTS_FOLDER = config['GENERAL']['SCRIPTS_FOLDER']

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=1)

def isadmin(ctx):
    if str(ctx.author.id) in [ADMIN]:
        return True
    else:
        print(f'{ctx.author.id} is not', ADMIN, type({ctx.author.id}), type(ADMIN) )
        return False


@bot.command()
async def restart(ctx, process):
    if not isadmin(ctx):
        return
    os.system(f"pm2 restart {process}")
    await ctx.send(f"Restarted {process}")

@bot.command()
async def script(ctx, process):
    if not isadmin(ctx):
        return
    try:
        output = subprocess.check_output(f"{process}", shell=True)
    except Exception as e:
        output = str(e)
    await ctx.send(f"Runing {output} ")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)
