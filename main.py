import discord
from discord.ext import commands
import configparser
import random

import os
import errno
import logging

from general_commands import General
from config import Config
from sounds import Music
from activity import Activity

#logger-------------------------------------------
client = discord.Client()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
#--------------------------------------------------

con = Config()

bot = commands.Bot(command_prefix='!', description="this is Partyfinderbot")


bot.add_cog(General(bot))
bot.add_cog(Music(bot))
bot.add_cog(Activity(bot))
bot.run(con.token)
