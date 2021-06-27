import discord
import os
import configparser

from discord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['GENERAL']['TOKEN']
ADMIN = config['GENERAL']['ADMIN']
PREFIX = config['GENERAL']['PREFIX']
SCRIPTS_FOLDER = config['GENERAL']['SCRIPTS_FOLDER']

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=1)

def isadmin(ctx):
    if ctx.author.id in [ADMIN]:  # THIS PART DOES NOT WORK AND USER ID HAS TO BE INSteAD OF ADMIN VARIABLE FOR NOW
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
    os.system(f"{SCRIPTS_FOLDER}{process}.sh")
    await ctx.send(f"Runing {process}.sh")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)
