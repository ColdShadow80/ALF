import discord
import os
import configparser

from discord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['GENERAL']['TOKEN']
ownerID = config['GENERAL']['ownerID']
PREFIX = config['GENERAL']['PREFIX']
SCRIPTS_FOLDER = config['GENERAL']['SCRIPTS_FOLDER']

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=1)

def isadmin(ctx):
    if ctx.author.id in [ownerID]:  # THIS PART DOES NOT WORK AND USER ID HAS TO BE INSteAD OF ADMIN VARIABLE FOR NOW
        return True
    else:
        print(f'{ctx.author.id} is not allowed, user does not match owner ID ', ownerID )
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
    await ctx.send(f"Runing {output}")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)
