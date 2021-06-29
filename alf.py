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
    if ctx.author.id in ADMIN:                                     
        return True                                                               
    else:                                                                         
        return False                                                              
                                                                                  
@bot.command()                                                                    
async def restart(ctx, process):                                                  
    if not isadmin(ctx):                                                          
        return                                                                    
    os.system(f"pm2 restart {process}")                                           
    await ctx.send(f"Restarted {process}")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    
bot.run(TOKEN)
